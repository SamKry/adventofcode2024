async function loadAlgorithms() {
  const daySelector = document.getElementById('day-selector');

  // Generate days 1 to 24
  const days = Array.from({ length: 24 }, (_, i) => i + 1);

  days.forEach(day => {
    const option = document.createElement('option');
    option.value = day;
    option.textContent = `Day ${day}`;
    daySelector.appendChild(option);
  });
}

function solveCurrentDay() {
  const day = document.getElementById('day-selector').value;
  const input = document.getElementById('input').value;

  if (!input) {
    alert('Please enter your input');
    return;
  }

  const outputDiv1 = document.getElementById('output-1');
  const outputDiv2 = document.getElementById('output-2');

  // Set UI feedback before computation starts
  outputDiv1.textContent = 'Solving...';
  outputDiv2.textContent = 'Solving...';

  // Use Web Worker for calculation
  const worker = new Worker('web/scripts/worker.js');

  worker.postMessage({ day, input });

  worker.onmessage = ({ data }) => {
    const { result1, result2, error } = data;

    if (error) {
      outputDiv1.textContent = `Solution for day ${day} question 1 not implemented yet :/`;
      outputDiv2.textContent = `Solution for day ${day} question 2 not implemented yet ):`;
      console.error(error);
    } else {
      outputDiv1.textContent = `${result1}`;
      outputDiv2.textContent = `${result2}`;
    }

    worker.terminate();
  };

  worker.onerror = (err) => {
    console.error('Worker error:', err);
    outputDiv1.textContent = `An error occurred while solving day ${day} question 1.`;
    outputDiv2.textContent = `An error occurred while solving day ${day} question 2.`;
    worker.terminate();
  };
}

document.getElementById('solve-button').addEventListener('click', solveCurrentDay);
loadAlgorithms();
