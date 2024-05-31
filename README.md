# Create an AI Slackbot with Django 

[Watch it now](https://www.youtube.com/watch?v=Rol2SR11oZU)

## Recommended skills

- **Python XP** - at least the first 15 days of [30 Days of Python](https://www.youtube.com/playlist?list=PLEsfXFp6DpzQjDBvhNy5YbaBx9j-ZsUe6)
- **Django XP** - the first 30 videos of the [Try Django playlist](https://www.youtube.com/playlist?list=PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL) or the [Your First Django Project course](https://www.codingforentrepreneurs.com/courses/your-first-django-project/)


## Prepare your Domain

Even in development, Slackbots require **https** domains so we'll be using Cloudflare Tunnels. Cloudflare Tunnels are free and incredibly effective. I used to use _ngrok_ but their free teir does not (or did not) offer custom domains like Cloudflare Tunnels. For an alternative tunnelling options, check out [this excellent repo](https://github.com/anderspitman/awesome-tunneling).

To use CloudFlare Tunnels, you need:

- Control over a domain name so you can update to Cloudflare nameservers (NS Records)
  - In my case, I have a domain I use just for development. When I added this domain to my Cloudflare account, I was prompted to use the Cloudflare nameservers `audrey.ns.cloudflare.com` and `trevor.ns.cloudflare.com` -- (yours may be different). Review [this guide](https://developers.cloudflare.com/dns/zone-setups/full-setup/setup/) for more).
- A free Cloudflare account
- Your domain name registered as a website on cloudflare which just means that you need to add your domain as a website so you can get the correct nameservers for it.
- Eventually, you will need to install `Cloudflared` which you can by going through the [official docs](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/downloads/)).

I will show you how to create the tunnel in the upcoming tutorial.
