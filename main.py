import argparse
from zlm import AutoApplyModel

def create_resume_cv(url, master_data, api_key, provider, model, downloads_dir):
    # Check for None values and set defaults
    url = url or "https://www.linkedin.com/jobs/view/4183333268"
    master_data = master_data or "/home/boson-264/Downloads/Someswar_Sivakavi_CV.pdf"
    api_key = "AIzaSyAgpVuOF2Jv37r5eqGeIRN3F3jf10ET2Is"
    provider = provider or "Gemini"
    model = model or "gemini-2.0-flash"
    downloads_dir = downloads_dir or "/home/boson-264/Downloads/"

    print(f"url: {url}")
    print(f"master_data: {master_data}")
    print(f"api_key: {api_key}")
    print(f"provider: {provider}")
    print(f"model: {model}")
    print(f"downloads_dir: {downloads_dir}")

    job_llm = AutoApplyModel(api_key, provider, model, downloads_dir)
    job_llm.resume_cv_pipeline(url, master_data)


if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser()

    # Add the required arguments
    parser.add_argument("-u", "--url", help="URL of the job posting")
    parser.add_argument("-m", "--master_data", help="Path of user's master data file.")
    parser.add_argument("-k", "--api_key", default="os", help="LLM Provider API Keys")
    parser.add_argument("-d", "--downloads_dir", help="Give detailed path of folder")
    parser.add_argument("-p", "--provider", help="LLM provider name. support for openai, gemini")
    parser.add_argument("-l", "--model", help="LLM model name")

    # Parse the arguments
    args = parser.parse_args()

    create_resume_cv(
        args.url, args.master_data, args.api_key, args.provider, args.model, args.downloads_dir
    )