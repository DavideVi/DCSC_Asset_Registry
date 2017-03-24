
# Scenario: Tagging data
import requests, os
from helper import load_payload


ENDPOINT = "http://52.56.141.168/api"

ASSET_ADD = ENDPONT + "/asset/add"

'''
Scenario: Tagging data
    Given we have valid information regarding an asset
    When we request to add an asset
    Then then the relevant tags should be extracted
'''

payload = load_payload("POST_asset_add.valid_payload.json")
respones = requests.post(ASSET_ADD, data=payload)


'''

  Scenario: Technology tags
    Given we have valid information regarding an asset
    And the asset uses various technologies
      | asset_name          | technologies      |
      | Docker migrator     | docker; bash;     |
      | Perl mongo migrator | perl; mongo;      |
    When we request to add an asset
    Then the technology tags should be generated for the asset

  Scenario: Author tags
    Given we have valid information regarding an asset
    And the asset has various authors
      | asset_name          | authors           |
      | Death star          | galen.marek;      |
      | The Agile Manifesto | Kent.Beck; Mike.Beedle; Arie.van.Bennekum; Alistair.Cockburn; Ward.Cunningham; Martin.Fowler; James.Grenning; Jim.Highsmith; Andrew.Hunt; Ron.Jeffries; Jon.Kern; Brian.Marick; Robert.C. Martin; Steve.Mellor; Ken.Schwaber; Jeff.Sutherland; Dave.Thomas; |
    When we request to add an asset
    Then the author tags should be generated for the asset

  Scenario: NLP tags
    Given we have valid information regarding an asset
    And the asset has a purpose
      | asset_name          | asset_purpose                                                         |
      | Car                 | Invention that allows individuals to travel faster between locations  |
    When we request to add an asset
    Then the noun, adjective and verb tags should be generated for the asset

'''
