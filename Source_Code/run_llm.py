import os
from openai import OpenAI
import anthropic
import cohere
import dashscope
import google.generativeai as genai
from mistralai import Mistral
from google.cloud import aiplatform
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential



class CallLLM():
    def __init__(self, params):
        self.model_params = params
        self.system_prompt = "You are an expert in Python programming. You are given a text specification surrounded by angle brackets. Create Python code according to the text specification. The Python code should not contain any comments. The Python code should be delimited only by triple backticks."
        self.prompt = ""
        

    def set_prompt(self, text, flag):
        if flag:
            self.prompt = self.system_prompt + (f"\n<{text}>")
        else:
            self.prompt = "<" + text + ">"


    def gemini(self):
        genai.configure(api_key=os.environ['GEMINI_API_KEY'])
        model = genai.GenerativeModel(
            model_name=self.model_params['model'],
            tools='code_execution'
            )
        response = model.generate_content(self.prompt, 
                                          generation_config=genai.types.GenerationConfig(candidate_count=1, max_output_tokens=self.model_params['max_tokens'], temperature=self.model_params['temperature'],),
                                          )
        
        return str(response), self.prompt
    

    def mistral(self):
        client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])
        response = client.chat.complete(
            model=self.model_params['model'], 
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user","content": self.prompt}
                ],
            max_tokens=self.model_params['max_tokens'],
            temperature=self.model_params['temperature'],      
        )

        return str(response), self.prompt
    

    def vertex_ai(self):
        region = "us-east1"
        client = aiplatform.gapic.PredictionServiceClient(client_options={"api_endpoint": f"{region}-aiplatform.googleapis.com"})
        PROJECT_ID = os.environ["VERTEX_AI_PROJECT_ID"]
        ENDPOINT_ID = os.environ["VERTEX_AI_ENDPOINT_ID"]
        prompt = f"""
        System: {self.system_prompt}
        User: {self.prompt}
        """
        instances = [
            {
                "prompt": prompt,
                "max_tokens": self.model_params['max_tokens'],
                "temperature": self.model_params['temperature'],
            },
            ]
        instances = instances if isinstance(instances, list) else [instances]
        instances = [
            json_format.ParseDict(instance_dict, Value()) for instance_dict in instances
            ]
        parameters_dict = {}
        parameters = json_format.ParseDict(parameters_dict, Value())
        endpoint = client.endpoint_path(project=PROJECT_ID, location=region, endpoint=ENDPOINT_ID)
        response = client.predict(endpoint=endpoint, instances=instances, parameters=parameters)

        return str(response), self.prompt
    

    def azure(self, model):
        if model=="Llama_3_405":
            api_key = os.getenv("AZURE_INFERENCE_CREDENTIAL", '')
            end_point = "https://Meta-Llama-3-1-405B-Instruct-jqt.eastus.models.ai.azure.com"
            message = [
                {
                "role": "system",
                "content": self.system_prompt
                },
                {
                "role": "user",
                "content": self.prompt
                },
            ]
        
        elif model=="Llama_3_70":
            api_key = os.getenv("AZURE_INFERENCE_CREDENTIAL_LLAMA70", '')
            end_point = "https://Meta-Llama-3-1-70B-Instruct-ofoo.eastus.models.ai.azure.com"
            message = [
                {
                "role": "system",
                "content": self.system_prompt
                },
                {
                "role": "user",
                "content": self.prompt
                },
            ]

        elif model=="Phi_3":
            api_key = os.getenv("AZURE_INFERENCE_CREDENTIAL_PHI", '')
            end_point = "https://Phi-3-medium-4k-instruct-pmihg.eastus2.models.ai.azure.com"
            message = [
                {
                "role": "system",
                "content": "You are an expert in Python programming."
                },
                {
                "role": "user",
                "content": f"You are given a text specification surrounded by angle brackets. Create Python code according to the text specification. The Python code should not contain any comments. The Python code should be delimited only by triple backticks. {self.prompt}"
                },
            ]

        client = ChatCompletionsClient(
            endpoint=end_point,
            credential=AzureKeyCredential(api_key)
            )
        
        payload = {
            "messages": message,
            "max_tokens": self.model_params['max_tokens'],
            "temperature": self.model_params['temperature'],
            }
        
        response = client.complete(payload)

        return str(response), self.prompt


    def openai_api(self):
        model_name = self.model_params['model']
        if "gpt" in model_name:
            client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)
        elif model_name == "deepseek-coder":
            client = OpenAI(api_key=os.environ.get("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")
        elif model_name == "databricks/dbrx-instruct" or model_name == "cognitivecomputations/dolphin-mixtral-8x22b":
            client = OpenAI(api_key=os.getenv("OPENROUTER_API_KEY"), base_url="https://openrouter.ai/api/v1",)
        elif model_name == "google/gemma-2-27b-it" or model_name == "Qwen/Qwen2.5-72B-Instruct" or model_name == "Qwen/Qwen2.5-Coder-32B-Instruct":
            client = OpenAI(api_key=os.getenv("DEEPINFRA_API_KEY"), base_url="https://api.deepinfra.com/v1/openai",)
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user","content": self.prompt}
                ],
            model=model_name,
            max_tokens=self.model_params['max_tokens'],
            temperature=self.model_params['temperature'],
        )

        return str(response), self.prompt
    

    def huggingface(self):
        model_name = self.model_params['model']
        if model_name == "starcoder2-15b-instruct-v0.1":
            client = OpenAI(api_key=os.getenv("HUGGING_FACE_API_KEY"), base_url="https://kul5fdqua17tzjt4.us-east-1.aws.endpoints.huggingface.cloud/v1/",)
        elif model_name == "qwen2.5-coder-7b-instruct":
            client = OpenAI(api_key=os.getenv("HUGGING_FACE_API_KEY"), base_url="https://qalhfph9apfyqp53.us-east-1.aws.endpoints.huggingface.cloud/v1/",)
        response = client.chat.completions.create(
            messages=[{"role": "user","content": self.prompt}],
            model="tgi",
            max_tokens=self.model_params['max_tokens'],
            temperature=self.model_params['temperature'],
        )

        return str(response), self.prompt



    def claude(self):
        client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        response = client.messages.create(
            model=self.model_params['model'],
            max_tokens=self.model_params['max_tokens'],
            temperature=self.model_params['temperature'],
            system=self.system_prompt,
            messages=[{"role": "user", "content": [{"type": "text", "text": self.prompt}]}]
        )

        return str(response), self.prompt


    def cohere(self):
        co = cohere.Client(os.environ.get("COHERE_API_KEY"),)
        response = co.chat(
            preamble=self.system_prompt,
            message=self.prompt,
            model=self.model_params['model'],
            max_tokens=self.model_params['max_tokens'],
            temperature=self.model_params['temperature'],
        )

        return str(response), self.prompt
    

    def qwen(self):
        dashscope.api_key = os.getenv("DASHSCOPE_API_KEY")
        dashscope.base_http_api_url = 'https://dashscope-intl.aliyuncs.com/api/v1'
        messages = [
            {'role': 'system', 'content': self.system_prompt},
            {'role': 'user', 'content': self.prompt}
            ]
        response = dashscope.Generation.call(
            self.model_params['model'],
            messages=messages,
            result_format='message',
            max_tokens=self.model_params['max_tokens'],
            temperature=self.model_params['temperature'],
            stream=False,
            output_in_full=False,
            )
        
        return str(response), self.prompt

    

    