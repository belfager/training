# Using escape sequence
bel_char = '\x07'
print(f"Using \\x07: {bel_char}")

# Using chr()
bel_char_chr = chr(7)
print(f"Using chr(7): {bel_char_chr}")

# Demonstrating the effect of the BEL character
# (This might not produce a visible output on all terminals, but it should trigger a sound)
#print("\a") # This is a common way to trigger the bell, but it might not work everywhere.
