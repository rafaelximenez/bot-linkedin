import argparse
from engine.linkedin import Linkedin
from engine.services.respondRecruiters import RespondRecruiters
import sys
import json

def start(args):
    linkedin = Linkedin()
    driver = linkedin.login()

    responde_recruiters = RespondRecruiters(driver)

    if args.responder_conexoes:
        responde_recruiters.accept_connections()  
    elif args.responder_recrutadores:
        with open("config.json", "r") as f:
            data = json.load(f)

        text = data["responder_recrutadores"]["text"]
        responde_recruiters.answer_job_invitations(text)

    sys.exit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="LinkedIn Automation Script")

    parser.add_argument("--responder_conexoes", action="store_true", help="Answer connection invitations")
    parser.add_argument("--responder_recrutadores", action="store_true", help="Answer job invitations")

    args = parser.parse_args()
    start(args)