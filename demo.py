from gradio_client import Client

client = Client("Walmart-the-bag/Juggernaut-X-v10")
result = client.predict(
		prompt="Elon musk riding a Tesla in mars",
		negative_prompt="",
		steps=50,
		guidance_scale=7.5,
		add_4k_masterpiece=True,
		api_name="/predict"
)
print(result)