from Adventurer import Adventurer
from Companion import Companion

# Create a Companion instance
my_companion = Companion("Rex", "Dog", ["fetch", "guard"])

# Create an Adventurer instance with the companion
adventurer = Adventurer("Jane", "Doe", ["jerky", "berries"], "companion food", my_companion)

# Adventurer interacts with their companion
adventurer.feed_companion()
adventurer.go_on_adventure()
adventurer.bathe_companion()
