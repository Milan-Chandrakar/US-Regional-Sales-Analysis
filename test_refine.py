s1 = 'HAL will approach Russia for approvals to the Super Sukhoi program after they finalize equipment and systems that will be upgraded on 150 units of Sukhoi-30MKI. Indian-made systems will be used while Russian components will be used for its engines. Payments have been held up due to western sanctions on Russian banks but HAL and IAF have confirmed that Russia has been able to maintain the pre-sanction era level of supply of spares for India'
s2 = 'Indian Air Force plans to equip 20 more Sukhoi-30MKI fighter jets with the Air-Launched BrahMos-A after successful trials, for which the Su-30MKI fuselage requires hardening in certain sections to carry the missile. The hardening process will be performed by HAL locally in India.'
s3 = "Hindustan Aeronautics Limited's Super Sukhoi upgrade program will not involve engine upgrades, according to sources. India has rejected offers to swap its AL-31F engines with AL-41F-1 engines due to the costs involved in setting up infrastructure and procurement, instead opting to execute the upgrade program locally due to Russian sanctions."

import openai
openai.api_key = "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"

prompt=f"""summarize the text {s3 + ' '+ s1 + ' ' + s2 }"""
response = openai.ChatCompletion.create(
model="gpt-3.5-turbo",
messages=[
    {"role": "system", "content": str(prompt)},
        ]
)
r = response['choices'][0]['message']['content']
print(r)