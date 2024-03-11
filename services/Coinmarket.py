import aiohttp
from schemas.models import Quote, Coin, NotFound


class CoinMarket:
    all_coin = {"Bitcoin", "Ethereum", "Tether USDt", "BNB", "Solana", "XRP", "USDC", "Cardano", "Dogecoin",
                "Shiba Inu", "Avalanche", "Polkadot", "Chainlink", "Polygon", "TRON", "Toncoin", "Bitcoin Cash",
                "Uniswap", "NEAR Protocol", "Litecoin", "Internet Computer", "Filecoin", "Ethereum Classic", "Dai",
                "UNUS SED LEO", "Cosmos", "Aptos", "Immutable", "Render", "Stacks", "Optimism", "Bittensor", "Cronos",
                "Hedera", "The Graph", "Stellar", "OKB", "Pepe", "Injective", "Theta Network", "Kaspa", "VeChain",
                "Mantle", "First Digital USD", "THORChain", "Lido DAO", "Celestia", "FLOKI", "Monero", "Arbitrum",
                "Arweave", "Maker", "Fantom", "Algorand", "Fetch.ai", "Sei", "Bitcoin SV", "Flow", "Gala", "Beam",
                "dogwifhat", "Bonk", "Aave", "Sui", "dYdX (Native)", "MultiversX", "The Sandbox", "Starknet", "Mina",
                "AxieInfinity", "BitTorrent (New)", "SingularityNET", "ORDI", "Decentraland", "Akash Network",
                "KuCoin Token", "Quant", "Worldcoin", "Tezos", "Flare", "Helium", "ApeCoin", "Synthetix", "Chiliz",
                "Axelar", "EOS", "eCash", "SATS", "TrueUSD", "Pyth Network", "Bitget Token", "Ronin", "Neo", "Conflux",
                "dYdX (ethDYDX)", "Oasis Network", "Kava", "WEMIX", "IOTA", "Gnosis"}

    def __init__(self, name_coin):
        self.name_coin = name_coin
        self.api_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': '5a7a63d0-48b9-4b20-8ec9-d22fa6d2ff8d',
        }

    async def get(self) -> Coin | NotFound:
        data = await self.get_price_coin()
        if data is None:
            return NotFound(er=404, msg=f"Not found {self.name_coin} coin")
        result = await self.parsing(data)
        return result

    async def parsing(self, data: dict) -> Coin:
        quote = Quote(**data["quote"]["USD"])
        coin = Coin(name=self.name_coin, symbol=data["symbol"], quote=quote)
        return coin

    def get_all_coins(self):
        return self.all_coin

    async def get_price_coin(self) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.api_url, headers=self.headers) as resp:
                response = await resp.json()
                response = response["data"]
                for el in response:
                    if el["name"] == self.name_coin:
                        return el
