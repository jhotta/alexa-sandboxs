from pyalexaskill.AlexaBaseHandler import AlexaBaseHandler


class AlexaDatadogHandler(AlexaBaseHandler):

    # Sample concrete implementation of the AlexaBaseHandler to test the
    # deployment scripts and process.
    # All on_ handlers call the same test response changing the request type
    # spoken.


    def __init__(self):
        super(self.__class__, self).__init__()
        self.card_title = "Test Datadog Response"


    def _test_response(self, msg):
        session_attributes = {}
        card_title = "Test Response"
        card_output = "Test card output"
        speech_output = "Welcome to the Python Alexa Test Deployment for request type {0}.  It seems to have worked".format(
            msg)
        # If the user either does not reply to the welcome message or says something
        # that is not understood, they will be prompted again with this text.
        reprompt_text = "Reprompt text for the Alexa Test Deployment"
        should_end_session = True

        speechlet = self._build_speechlet_response(card_title, card_output, speech_output, reprompt_text,
                                                   should_end_session)

        return self._build_response(session_attributes, speechlet)


    def on_processing_error(self, event, context, exc):
        session_attributes = {}
        speech_output = "I am having difficulty fulfilling your request."

        reprompt_text = "I did not hear you"
        should_end_session = True

        if exc:
            speech_output = "I am having difficulty fulfilling your request. {0}".format(exc.message)

        card_output = speech_output
        speechlet = self._build_speechlet_response(self.card_title,
                                                   card_output,
                                                   speech_output,
                                                   reprompt_text,
                                                   should_end_session)

        return self._build_response(session_attributes, speechlet)


    def on_launch(self, launch_request, session):
        session_attributes = {}
        card_output = "Sample Card Output"
        speech_output = "Sample Speech Output"

        reprompt_text = "I did not hear you"
        should_end_session = False
        speechlet = self._build_speechlet_response(self.card_title,
                                                   card_output,
                                                   speech_output,
                                                   reprompt_text,
                                                   should_end_session)

        return self._build_response(session_attributes, speechlet)


    def on_session_started(self, session_started_request, session):
        return self._test_response("on session started")


    def on_intent(self, intent_request, session):
        response = None
        session_attributes = {}
        reprompt_text = "I did not hear you sample"
        should_end_session = True
        card_output = "Sample Card Output"
        intent_name = self._get_intent_name(intent_request)

        if intent_name == "DatadogGetIntent":
            deployment_env = self._get_deployment_env(intent_request)

            if deployment_env in ["prod", "production"]:
                speech_output = "The prod is running just fine!"
            elif deployment_env in ["stage", "staging"]:
                speech_output = "Someone had just launched, 1,000 instances on the staging!"
            else:
                speech_output = "Which environment do you want to know?"

            speechlet = self._build_speechlet_response(self.card_title,
                                                       card_output,
                                                       speech_output,
                                                       reprompt_text,
                                                       should_end_session)

            response = self._build_response(session_attributes, speechlet)

        elif intent_name == "DatadogSetIntent":
            speech_output = "Requested setting is Done!"
            speechlet = self._build_speechlet_response(self.card_title,
                                                       card_output,
                                                       speech_output,
                                                       reprompt_text,
                                                       should_end_session)

            response = self._build_response(session_attributes, speechlet)

        elif intent_name == "DatadogEmployeeIntent":
            employee_name = self._get_employee_name(intent_request)

            if employee_name in ["jay", "naotaka", "hotta"]:
                speech_output = "Jay Hotta, is the first Datadog employee, in Japan"
            elif employee_name in ["alexis"]:
                speech_output = "Alexis, is Our co-funder, and, CTO."
            elif employee_name in ["masa", "hattori"]:
                speech_output = "Masa, is Our newest! and, Japan based. employee."
            else:
                speech_output = "Huuuum... We do not know whom you asked?"

            speechlet = self._build_speechlet_response(self.card_title,
                                                       card_output,
                                                       speech_output,
                                                       reprompt_text,
                                                       should_end_session)

            response = self._build_response(session_attributes, speechlet)

        elif intent_name == "DatadogBestEmployeeIntent":
            speech_output = "Jay Hotta, is the best!"
            speechlet = self._build_speechlet_response(self.card_title,
                                                       card_output,
                                                       speech_output,
                                                       reprompt_text,
                                                       should_end_session)

            response = self._build_response(session_attributes, speechlet)

        else:
            raise ValueError("Invalid intent")

        return response

    def on_session_ended(self, session_end_request, session):
        return self._test_response("on session end")

    def on_help_intent(self, intent_request, session):
        session_attributes = {}
        card_output = "Card Help"
        speech_output = "Speech Help"

        reprompt_text = "I did not hear you, {0}".format(speech_output)
        should_end_session = False
        speechlet = self._build_speechlet_response(self.card_title,
                                                   card_output,
                                                   speech_output,
                                                   reprompt_text,
                                                   should_end_session)

        return self._build_response(session_attributes, speechlet)

    def on_stop_intent(self, intent_request, session):
        return self.on_cancel_intent(intent_request, session)

    def on_cancel_intent(self, intent_request, session):
        session_attributes = {}
        card_output = "Thank you and Good-bye"
        speech_output = "Thank you and Good-bye"

        reprompt_text = "{0}".format(speech_output)
        should_end_session = True
        speechlet = self._build_speechlet_response(self.card_title,
                                                   card_output,
                                                   speech_output,
                                                   reprompt_text,
                                                   should_end_session)

        return self._build_response(session_attributes, speechlet)

    def on_no_intent(self, intent_request, session):
        return self._test_response("on no intent")

    def on_yes_intent(self, intent_request, session):
        return self._test_response("on yes intent")

    def on_repeat_intent(self, intent_request, session):
        return self._test_response("on repeat intent")

    def on_start_over_intent(self, intent_request, session):
        return self._test_response("on start over intent")

    def _get_employee_name(self, intent_request):
        intent = self._get_intent(intent_request)

        if intent is not None and 'value' in intent['slots']['EmployeeName']:
            employee_name = intent['slots']['EmployeeName']['value']
        else:
            employee_name = None

        return employee_name

    def _get_deployment_env(self, intent_request):
        intent = self._get_intent(intent_request)

        if intent is not None and 'value' in intent['slots']['DeploymentEnv']:
            deployment_env = intent['slots']['DeploymentEnv']['value']
        else:
            deployment_env = None

        return deployment_env