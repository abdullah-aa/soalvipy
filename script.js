const BUBBLE_SORT_RESPONSE = [[8, 9, 7, 2, 10, 1, 4, 6, 5, 3], [8, 9, 9, 2, 10, 1, 4, 6, 5, 3], [8, 8, 9, 2, 10, 1, 4, 6, 5, 3], [7, 8, 9, 2, 10, 1, 4, 6, 5, 3], [7, 8, 9, 9, 10, 1, 4, 6, 5, 3], [7, 8, 8, 9, 10, 1, 4, 6, 5, 3], [7, 7, 8, 9, 10, 1, 4, 6, 5, 3], [2, 7, 8, 9, 10, 1, 4, 6, 5, 3], [2, 7, 8, 9, 10, 1, 4, 6, 5, 3], [2, 7, 8, 9, 10, 10, 4, 6, 5, 3], [2, 7, 8, 9, 9, 10, 4, 6, 5, 3], [2, 7, 8, 8, 9, 10, 4, 6, 5, 3], [2, 7, 7, 8, 9, 10, 4, 6, 5, 3], [2, 2, 7, 8, 9, 10, 4, 6, 5, 3], [1, 2, 7, 8, 9, 10, 4, 6, 5, 3], [1, 2, 7, 8, 9, 10, 10, 6, 5, 3], [1, 2, 7, 8, 9, 9, 10, 6, 5, 3], [1, 2, 7, 8, 8, 9, 10, 6, 5, 3], [1, 2, 7, 7, 8, 9, 10, 6, 5, 3], [1, 2, 4, 7, 8, 9, 10, 6, 5, 3], [1, 2, 4, 7, 8, 9, 10, 10, 5, 3], [1, 2, 4, 7, 8, 9, 9, 10, 5, 3], [1, 2, 4, 7, 8, 8, 9, 10, 5, 3], [1, 2, 4, 7, 7, 8, 9, 10, 5, 3], [1, 2, 4, 6, 7, 8, 9, 10, 5, 3], [1, 2, 4, 6, 7, 8, 9, 10, 10, 3], [1, 2, 4, 6, 7, 8, 9, 9, 10, 3], [1, 2, 4, 6, 7, 8, 8, 9, 10, 3], [1, 2, 4, 6, 7, 7, 8, 9, 10, 3], [1, 2, 4, 6, 6, 7, 8, 9, 10, 3], [1, 2, 4, 5, 6, 7, 8, 9, 10, 3], [1, 2, 4, 5, 6, 7, 8, 9, 10, 10], [1, 2, 4, 5, 6, 7, 8, 9, 9, 10], [1, 2, 4, 5, 6, 7, 8, 8, 9, 10], [1, 2, 4, 5, 6, 7, 7, 8, 9, 10], [1, 2, 4, 5, 6, 6, 7, 8, 9, 10], [1, 2, 4, 5, 5, 6, 7, 8, 9, 10], [1, 2, 4, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]];
// const worker = new Worker('worker.js');

// worker.postMessage(BUBBLE_SORT_RESPONSE[0]['main_frame']);

// worker.onmessage = e => {
//     console.log(e.data);
// }

const DISPLAY = document.getElementById('display');
const DISPLAY_DIMENSTION = 300;
const TOP_OFFSET = 10;
const ctx = DISPLAY.getContext('2d');
const element_edge = Math.floor(DISPLAY_DIMENSTION / BUBBLE_SORT_RESPONSE[0].length);
const base_margin = Math.floor(element_edge * 0.1);
const base_edge = Math.floor(element_edge * 0.8);

const getRectColors = (arr1, arr2) => arr1.map((elem, index) => arr2[index] !== elem ? 'blue' : 'red');

const drawRects = (numbers, colors) => {
    ctx.clearRect(0, 0, DISPLAY_DIMENSTION, DISPLAY_DIMENSTION);
    numbers.forEach((number, index) => {
        let rectX = (index * element_edge) + base_margin;
        let rectY = TOP_OFFSET + DISPLAY_DIMENSTION - (number * element_edge);
        let rectH = number * element_edge;
        ctx.fillStyle = colors[index];
        ctx.fillRect(rectX, rectY, base_edge, rectH);
    });
}

let frame_counter = 0;
intervalID = setInterval(() => {
    if (frame_counter < BUBBLE_SORT_RESPONSE.length) {
        let colors = getRectColors(BUBBLE_SORT_RESPONSE[frame_counter], BUBBLE_SORT_RESPONSE[BUBBLE_SORT_RESPONSE.length > (frame_counter + 1)? frame_counter + 1 : frame_counter])
        drawRects(BUBBLE_SORT_RESPONSE[frame_counter], colors);
        frame_counter++;
    } else {
        clearInterval(intervalID);
    }
}, 1000);


