
input <- readLines('input.txt')

input <- as.numeric(input)

# Part 1 ---------------------------------------------------------------------
totals = c(0)
current = 0
for (i in aoc_input) {
  if (is.na(i)) {
    totals = append(totals, current)
    current = 0
    next
    
  }
    current = current + i
}
max(totals)


# Part 2 ---------------------------------------------------------------------
sum(sort(totals, decreasing = TRUE)[1:3])