
import { socket } from "./socket.mjs";
console.log("THIS IS HOME.js")

const btn = document.getElementById("btn");
console.log(btn)
if (!btn){
}
btn.onclick = function(){
    console.log("BTN CLICKED")
    socket.emit("player_move", {data: "I am connected"});

}
    

socket.on("board_update", (data) => {
    console.log("RECEIVED BOARD_UPDATE")
    updateBoardDisplay(data.board_config);
});


function updateBoardDisplay(board) {
    // Example: clear board container and re-render
    const boardDiv = document.getElementById("board");
    boardDiv.innerHTML = "";

    for (let row = 0; row < board.length; row++) {
        let rowDiv = document.createElement("div");
        for (let col = 0; col < board[row].length; col++) {
            let cell = document.createElement("span");
            cell.textContent = board[row][col];
            cell.style.padding = "10px";
            rowDiv.appendChild(cell);
        }
        boardDiv.appendChild(rowDiv);
    }
}