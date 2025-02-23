
    let phrases = [
        {% for phrase in motivation %}
            "{{ phrase }}",
        {% endfor %}
    ];
    let currentPhraseIndex = 0;
    const motivationText = document.getElementById('motivation-text');

    function getRandomPhrase() {
        return phrases[Math.floor(Math.random() * phrases.length)];
    }

    function changePhrase() {
        motivationText.textContent = getRandomPhrase();
    }

    setInterval(changePhrase, 10000); // Меняем фразу каждые 10 секунд


        document.addEventListener('DOMContentLoaded', function() {
        const alerts = document.querySelectorAll('.alert');

        alerts.forEach(alert => {
            // Инициализация анимации
            setTimeout(() => {
                alert.classList.add('show');
            }, 50); // Небольшая задержка для активации перехода

            // Убираем сообщение
            setTimeout(() => {
                alert.classList.remove('show');
                alert.classList.add('hide');

                // Удаление элемента после анимации
                setTimeout(() => {
                    alert.remove();
                }, 800); // Совпадает с длительностью анимации 0.8s
            }, 4000);
        });
    });