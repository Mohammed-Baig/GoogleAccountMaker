from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask

api_key = '174faff8fbc769e94a5862391ecfd010'
site_key = '6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-'  # grab from site
url = 'https://www.google.com/recaptcha/api2/demo'

client = AnticaptchaClient(api_key)
task = NoCaptchaTaskProxylessTask(url, site_key)
job = client.createTask(task)
job.join()
print (job.get_solution_response())