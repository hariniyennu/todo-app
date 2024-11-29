const addButton = document.getElementById('add-btn');
const taskInput = document.getElementById('todo-input');
const taskList = document.getElementById('todo-list');
const todoForm = document.getElementById('todo-form');

function addTask(event) {
    event.preventDefault();
    const taskText = taskInput.value.trim();
    if (taskText !== "") {
        const taskItem = document.createElement('li');
        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.classList.add('checkbox');
        checkbox.onclick = function () {
            if (checkbox.checked) {
                taskItem.classList.add('strike'); // Add strike-through style
            } else {
                taskItem.classList.remove('strike'); // Remove strike-through style
            }
        };

        const taskTextNode = document.createElement('span');
        taskTextNode.textContent = taskText;

        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete';
        deleteButton.classList.add('delete-btn');
        deleteButton.onclick = function () {
            taskItem.remove();
        };
        taskItem.appendChild(checkbox);
        taskItem.appendChild(taskTextNode);
        taskItem.appendChild(deleteButton);
        taskList.appendChild(taskItem);
        taskInput.value = "";
    } else {
        alert("Please enter a task.");
    }
}
todoForm.addEventListener('submit', addTask);
