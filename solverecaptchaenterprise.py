#pip3 install anticaptchaofficial

from anticaptchaofficial.recaptchav3enterpriseproxyless import *

site_key = '6LeNRRsbAAAAAEOyIR4EyXHfUTJAw9r5WAItrETf'
api_anticaptcha_key = '3b939cd231a2d6e72d11d611076d82e4'
current_url = 'https://www.avis.com'

solver = recaptchaV3EnterpriseProxyless()
solver.set_verbose(1)
solver.set_key(api_anticaptcha_key)
solver.set_website_url(current_url)
solver.set_website_key(site_key)
# solver.set_page_action("home_page")
solver.set_min_score(0.9)

# Specify softId to earn 10% commission with your app.
# Get your softId here: https://anti-captcha.com/clients/tools/devcenter
solver.set_soft_id(0)

g_response = solver.solve_and_return_solution()
if g_response != 0:
    print("g-response: "+g_response)
else:
    print ("task finished with error "+solver.error_code)