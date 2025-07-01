from recommender.data_loader import load_outfits
from recommender.outfit_logic import recommend_outfit

def main():
    outfits = load_outfits("data/outfits.json")
    outfit = recommend_outfit(outfits, outfit_type="casual")  # Try "formal", "sport"
    if outfit:
        print(f"Recommended Outfit ({outfit['type']}): {', '.join(outfit['items'])}")
    else:
        print("No outfit found for the given type.")

if _name_ == "_main_":
    main()
import json

def load_outfits(path="data/outfits.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Could not find outfit data file.")
        return []
    import random

def recommend_outfit(outfits, outfit_type=None):
    if outfit_type:
        filtered = [o for o in outfits if o["type"] == outfit_type]
    else:
        filtered = outfits

    return random.choice(filtered) if filtered else None
[
  {
    "type": "casual",
    "items": ["jeans", "t-shirt", "sneakers"]
  },
  {
    "type": "formal",
    "items": ["blazer", "shirt", "oxfords"]
  },
  {
    "type": "sport",
    "items": ["tracksuit", "running shoes"]
  }
]
