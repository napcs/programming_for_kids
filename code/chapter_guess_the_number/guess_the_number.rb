puts "Guess The Number!"
puts "----"

puts "I can guess a number between 1 and any number you give me."
puts "What's the highest number I should pick?"

number = gets

puts "Ok, I will guess a number between 1 and " + number
number = number.to_i - 1

computer_number =  rand(number.to_i) + 1

winner = false

while winner == false
  puts "Ok, guess the number!"
  guess = gets.to_i
  if guess == computer_number
    puts "You got it!"
    winner = true
  else
    if guess < computer_number
      puts "Too low. Try again!"
    else
      puts "Too high. Try again!"
    end
  end
end

