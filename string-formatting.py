name = 'Aso'

# The template
greeting = 'Hello, {}'

with_name = greeting.format(name)
with_name_two = greeting.format('World')

print(with_name)
print(with_name_two)

# The template
longer_phrase = 'Hello, {}. Today is {}.'
formatted = longer_phrase.format('guys', 'saturday')

print(formatted)
