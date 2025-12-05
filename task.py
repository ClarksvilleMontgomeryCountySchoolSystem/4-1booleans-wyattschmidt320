# THEORY: Why Positive Boolean Names Matter
# ============================================

# Remember our standing activity? Some questions were easy, others confusing.

# EASY QUESTIONS (Clear and positive):
# ✅ "Are you wearing shoes?"
# ✅ "Did you eat breakfast?"
# ✅ "Are you feeling awake?"

# HARD QUESTIONS (Negative and confusing):
# ❌ "Are you NOT wearing a hat?"
# ❌ "Did you NOT forget your homework?"
# ❌ "Are you NOT tired?"

# What made the hard questions difficult?
# - Your brain had to process the truth FIRST
# - Then FLIP it because of the "NOT"
# - That's double work!


# In Python, we store True/False values in variables.
# Just like those questions, variable NAMES matter!

# Compare these:
is_wearing_shoes = True     # Clear! Easy to understand
not_wearing_hat = True      # Wait... so they ARE wearing a hat? Confusing!

print("is_wearing_shoes =", is_wearing_shoes)  # You can see the value
print("not_wearing_hat =", not_wearing_hat)    # Still confusing to read!


# Here's the key insight:
# POSITIVE variable names don't mean the value is always True.
# They mean the NAME describes a positive state.

is_wearing_shoes = True     # Wearing shoes
is_wearing_shoes = False    # Not wearing shoes (but name is still positive/clear!)

not_tired = True            # Does this mean tired or NOT tired? 🤔
not_tired = False           # Now I'm really confused!

is_awake = True             # Clear: awake
is_awake = False            # Clear: not awake (sleepy)


# Try changing the values above and running the code!
# Notice how positive variable names stay clear no matter the value.# Paste code below then Commit changes [green button]
