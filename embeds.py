import discord


def embed_error(mensaje:str):
    embed = discord.Embed(
        title =f"Error",
        description = mensaje,
        color = discord.Color.red(),
        timestamp = discord.utils.utcnow(),
    )
    embed.set_author(name= "",icon_url="https://i.postimg.cc/dVRBHkqk/blockchainbot-foto.jpg")
    embed.set_thumbnail(url="https://images.icon-icons.com/2429/PNG/512/ethereum_logo_icon_147293.png")#"https://images.icon-icons.com/1384/PNG/512/eth-crypto-cryptocurrency-cryptocurrencies-cash-money-bank-payment_95149.png")
    return embed

def embed_exito(mensaje:str):
    embed = discord.Embed(
        title = "Exito",
        description = mensaje,
        color = discord.Color.green(),
        timestamp = discord.utils.utcnow(),
    )
    embed.set_author(name= "",icon_url="https://i.postimg.cc/dVRBHkqk/blockchainbot-foto.jpg")
    embed.set_thumbnail(url="https://images.icon-icons.com/2429/PNG/512/ethereum_logo_icon_147293.png")
    embed.set_footer(icon_url="https://cdn-icons-png.flaticon.com/512/1828/1828640.png", text= "")
    return embed

def embed_mostrar(mensaje:str):
    embed = discord.Embed(


        
    )

