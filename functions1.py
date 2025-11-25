from web3 import Web3
from discord import app_commands
import discord
from func_wallets import cargar_wallets

def wallet_valida(wallet):
    return Web3.is_address(wallet)

async def autocomplete_wallets(interaction: discord.Interaction, current : str):#Las funciones de autocompletado deben ser async porque responden a interacciones de Discord, que son asincronas.
    data = cargar_wallets()
    user_id = str(interaction.user.id)

    if user_id not in data:
        return []
    wallets = data[user_id]

    resultados = [
        app_commands.Choice(name=w, value=w) #name lo que ve el user, value lo que recibe la funcion
        for w in wallets if current.lower() in w.lower()
    ]

    return resultados[:25] #max de 25 wallets
async def autocomplete_stablecoin(interaction, current):
    stablecoins = ["USDT", "USDC", "DAI"]
    return [
        app_commands.Choice(name=stable, value=stable)
        for stable in stablecoins if current.lower() in stable.lower() #esta en 2 lineas, sino se puede hacer un for y if separado
    ]