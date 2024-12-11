async function loadAlgorithms() {
  const daySelector = document.getElementById('day-selector');

  // 24 ...1
  const days = Array.from({ length: 24 }, (_, i) => 24 - i);

  days.forEach(day => {
    const option = document.createElement('option');
    option.value = day;
    option.textContent = `Day ${day}`;
    daySelector.appendChild(option);
  });
}

async function solveCurrentDay() {
  const day = document.getElementById('day-selector').value;
  const input = document.getElementById('input').value;
  const outputDiv1 = document.getElementById('output-1');
  const outputDiv2 = document.getElementById('output-2');

  try {
    const module = await import(`../../javascript/${day}.js`);
    const result1 = module.solve1(input);
    const result2 = module.solve2(input);
    outputDiv1.textContent = `${result1}`;
    outputDiv2.textContent = `${result2}`;
  } catch (error) {
    outputDiv1.textContent = `Solution for day ${day} question 1 not implemented yet :/`;
    outputDiv2.textContent = `Solution for day ${day} question 2 not implemented yet ):`;
    console.error(error);
  }
}

document.getElementById('solve-button').addEventListener('click', solveCurrentDay);
loadAlgorithms();
