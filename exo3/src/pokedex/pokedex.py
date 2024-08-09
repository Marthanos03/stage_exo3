import httpx
import json
import logging
import typer
from rich import print


logger = logging.getLogger(__name__)


def main(pkm_name, debug: bool = False) -> int:
    """get informations about the pokemon given in argument"""

    if debug:
        logging.basicConfig(filename="logs.log", level=logging.DEBUG)
    else:
        logging.basicConfig(filename="logs.log", level=logging.INFO)

    if not isinstance(pkm_name, str):
        logger.error("TypeError: pkm_name should be a string")
        raise TypeError("pkm_name should be a string")

    with httpx.Client() as client:
        url1 = "https://pokeapi.co/api/v2/pokemon/"
        url2 = "https://pokeapi.co/api/v2/pokemon-species/"
        logger.debug("Requests send")
        r1 = client.get(url1 + pkm_name)
        r2 = client.get(url2 + pkm_name)
        logger.debug(
            "Requests received, status code "
            + str(r1.status_code)
            + " and "
            + str(r2.status_code)
        )

    if r1.status_code != 200:
        print(
            "A request failed. The pokemon name may be incorrect"
            + ", status code: "
            + str(r1.status_code)
        )
        logger.error(
            "A request failed. The pokemon name may be incorrect"
            + ", status code: "
            + str(r1.status_code)
        )
        return r1.status_code

    pokemon = json.loads(r1.text)
    species = json.loads(r2.text)

    en_description = []
    for e in species["flavor_text_entries"]:
        if e["language"]["name"] == "en":
            en_description.append(e["flavor_text"])

    print("[bold]" + pokemon["name"] + "[/bold]")
    print("pokemon no " + str(pokemon["id"]))
    print(en_description[-1])

    print("[bold]type[/bold]:")
    for slot in pokemon["types"]:
        print("   " + "[bold cyan]"+slot["type"]["name"] +
              "[/bold cyan]")

    print("[bold]height[/bold]: " + str(pokemon["height"] / 10) + " m")
    print("[bold]weight[/bold]: " + str(pokemon["weight"] / 10) + " kg")

    print("[bold]stats[/bold]:")
    for stat in pokemon["stats"]:
        print("   " + str(stat["base_stat"]) + " " + stat["stat"]["name"])

    return r1.status_code


if __name__ == "__main__":
    typer.run(main)
