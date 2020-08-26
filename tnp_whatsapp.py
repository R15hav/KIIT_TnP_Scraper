from twilio.rest import Client

class whatsapp:
        def send_text(self,pay_load):
            # client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
            client = Client()

            # this is the Twilio sandbox testing number
            from_whatsapp_number='Twilio sandbox no.'
            # replace this number with your own WhatsApp Messaging number
            to_whatsapp_number='Put your phone no.'

            if pay_load=='No new notice':
                client.messages.create(body=pay_load,
                                    from_=from_whatsapp_number,
                                    to=to_whatsapp_number)
            else:
                for i in pay_load:
                    client.messages.create(body=i[0]+'\n'+'*'+i[1]+'*'+'\n'+i[2],
                                        from_=from_whatsapp_number,
                                        to=to_whatsapp_number)