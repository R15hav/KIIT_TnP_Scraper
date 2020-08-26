import kiit_code
import tnp_whatsapp
if __name__ == "__main__":
        sc=kiit_code.scrape()
        wp=tnp_whatsapp.whatsapp()
        sc.start_sel()
        sc.login()
        sc.parse()
        pay_load=sc.get_values()
        wp.send_text(pay_load)
