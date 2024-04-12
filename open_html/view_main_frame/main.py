async def main_frame():
    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Управление модами Minecraft</title>
    </head>
    <body>
        <form id="uploadForm" enctype="multipart/form-data">
            <input type="text" id="fileName" name="name" placeholder="Имя файла">
            <input type="file" id="fileInput" name="file" accept=".jar" required>
            <button type="submit" onclick="uploadFile(event)">Загрузить файл</button>
        </form>
        <p>
            <label id="textEnable">Автообновление выключено</label>
        </p>
        <p>
            <button type="submit" onclick="restartMods(event)">Открыть консоль сервера</button>
            <button type="submit" onclick="startServer(event)">Включить сервер</button>
            <button type="submit" onclick="stopServer(event)">Выключить сервер</button>
            </p>
        <p>
            <button type="submit" onclick="restartMods(event)">Обновить список модов</button>
            <button type="submit" onclick="autorestart(event)">Включить\Выключить автообновление модов</button>
            <button type="submit" onclick="uploadZip(event)">Скачать все моды</button>
        </p>
        <div id="records">
            <!-- Записи будут отображаться здесь -->
        </div>

        <script>
            autres = false
            let host = "eco-74.online:5435"
            let host1 = "eco-74.online:5436"
            function restartMods() {
                fetch(`http://${host1}/api/file`, {
                    method: 'GET',
                })
                .then(response => {
                    if (response.ok) {
                        return response.json();
                    } else {
                        throw new Error('Ошибка при получении данных!');
                    }
                })
                .then(data => {
                    let mods = data.mods;
                    let recordsDiv = document.getElementById('records');
                    recordsDiv.innerHTML = ''; // Очищаем список перед обновлением
                    mods.forEach(mod => {
                        let recordElem = document.createElement('div');
                        let deleteButton = document.createElement('button');
                        deleteButton.textContent = "Удалить";
                        deleteButton.onclick = function() { deleteRecord(mod.id, mod.name); }; // Передаем id и имя для удаления
                        recordElem.textContent = mod.name;
                        recordElem.appendChild(deleteButton);
                        recordsDiv.appendChild(recordElem);
                    });
                })
                .catch(error => console.error('Произошла ошибка:', error));
            }

            function startServer() {
                fetch(`http://${host}/api/server/start`, {
                    method: 'GET',
                })
                .then(response => {
                    if (response.ok) {
                        return response.json();
                    } else {
                        throw new Error('Ошибка при получении данных!');
                    }
                })
                .then(response => {
                    return response.json().then(data => {
                        restartMods();
                        if(response.ok){
                            alert("Сервер успешно отправлен на запуск");
                        } else {
                        alert("Ошибка!");
                        }
                    });
                })
                .catch(error => alert("Сервер успешно отправлен на запуск"));
            }

            function stopServer() {
                fetch(`http://${host}/api/server/stop`, {
                    method: 'GET',
                })
                .then(response => {
                    if (response.ok) {
                        return response.json();
                    } else {
                        throw new Error('Ошибка при получении данных!');
                    }
                })
                .then(response => {
                    return response.json().then(data => {
                        restartMods();
                        if(response.ok){
                            alert("Сервер успешно останвлен");
                        } else {
                        alert("Ошибка!");
                        }
                    });
                })
                .catch(error => alert("Сервер успешно останвлен"));
            }

            var myTimer;
            function autorestart(event) {
                if(autres){
                    clearInterval(myTimer)
                    autres = false
                    document.getElementById("textEnable").textContent="Автообновление выключено"
                }
                else {
                    myTimer = setInterval(restartMods,200);
                    autres = true
                    document.getElementById("textEnable").textContent="Автообновление включено"
                }
              }


            document.addEventListener('DOMContentLoaded', function() {
                restartMods();
            });

            function uploadFile(event) {
                event.preventDefault();
                let fileInput = document.getElementById('fileInput');
                let fileName = document.getElementById('fileName').value;
                fileName = fileInput.value;
                if (!fileInput.files.length || !fileName) {
                    alert('Пожалуйста, выберите файл и введите его название.');
                    return;
                }
                let formData = new FormData();
                formData.append('name', fileName);
                formData.append('file', fileInput.files[0]);
                fetch(`http://${host}/api/file`, {
                    method: 'POST',
                    body: formData
                })
                .then(response => {
                    return response.json().then(data => {
                        restartMods();
                        if(response.ok){
                            alert("Успешное добавление мода");
                        } else {
                        alert("Ошибка добавления мода");
                        }
                    });
                })
                .catch(error => alert("Работа с модом выполнена успешно"));
            }



        function uploadZip(event) {
            window.open(`http://${host}/api/file/upload`)
            }



            function deleteRecord(id, name) {
                let confirmation = confirm("Вы уверены, что хотите удалить запись: " + name + "?");
                if (confirmation) {
                    fetch(`http://${host}/api/file`, {
                        method: 'DELETE',
                        body: JSON.stringify({ name: name }), // Передаем имя для удаления
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    })
                    .then(response => {
                        if (response.ok) {
                            return response.json();
                        } else {
                            throw new Error('Ошибка при удалении данных!');
                        }
                    })
                    .then(data => {
                        restartMods();
                        alert("Запись успешно удалена.");
                        // После успешного удаления обновляем список модов

                    })
                    .catch(error => console.error('Произошла ошибка при удалении:', error));
                }
            }
        </script>
    </body>
    </html>
    """