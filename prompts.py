system_message = """
        You are the assistant of a transport manager who dispatches a lot of truck transport across europe.
"""


def generate_prompt(evaluation):
    prompt = f"""
        During the day the truck drivers are sending images of the loaded truck to confirm the loading security. 
        The second assistant of the transport manager evaluates these images whether the loadings are actually safe.
        But actually they are not always loaded safely. So he creates a evaluation which you can find here {evaluation}.
        If the loading security is bad the transport must not be started and the driver must ensure that the loading is 
        fulfills all safety instructions.

        Now your job is to use this evaluation from your colleague as basis for deciding if you should create a warning for the transport manager
        so he stops the driver from starting his road journey. The warning should be pretty concise and short and describe what's the problem
        and give potential advice for further action. Create this warning only if the loading safety is bad... if the loading is good create nothing.
    """
    return prompt