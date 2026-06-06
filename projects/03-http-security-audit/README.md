# 🔒 Проект 3: Аудит безопасности HTTP-заголовков (ручной анализ)

## 🎯 Цель задачи
Провести ручной аудит безопасности HTTP-заголовков трёх веб-ресурсов с использованием встроенных инструментов браузера и curl.

## 🛠️ Использованные инструменты
- **Browser DevTools** (вкладка Network → Headers)
- **curl** (команда `curl -I` для получения заголовков)

## 📋 Методология
Для каждого сайта проверялось наличие 5 ключевых заголовков безопасности:
1. Content-Security-Policy (CSP) — защита от XSS
2. X-Frame-Options — защита от Clickjacking
3. X-Content-Type-Options — защита от MIME-сниффинга
4. Strict-Transport-Security (HSTS) — принудительный HTTPS
5. Referrer-Policy — контроль утечки URL

## 📊 Результаты аудита

### Сайт 1: google.com
- **Присутствующие заголовки:**
content-security-policy
x-frame-options
x-content-type-options
strict-transport-security
referrer-policy
- **Отсутствующие заголовки:** 
нет
- **Вывод:** Высокий уровень защиты.

### Сайт 2: example.com
- **Присутствующие заголовки:** 
Referrer Policy
- **Отсутствующие заголовки:** 
content-security-policy
x-frame-options
x-content-type-options
strict-transport-security
- **Вывод:** Минимальная защита.
### Сайт 3: dstu.ru
- **Присутствующие заголовки:** 
Referrer Policy
x-content-type-options
x-frame-options
- **Отсутствующие заголовки:** 
strict-transport-security
content-security-policy
- **Вывод:** Средний уровень защиты.

## 🚨 Общие выводы
- Самый защищённый сайт: google.com
- Самый уязвимый сайт: example.com
- Чаще всего отсутствует:
x-content-type-options
strict-transport-security
- Рекомендации:
  1. Внедрить Content-Security-Policy для защиты от XSS
  2. Добавить Strict-Transport-Security для принудительного HTTPS
  3. Настроить X-Frame-Options для защиты от Clickjacking

## 📎 Приложения
- `screenshot_1.png` — заголовки google.com (из DevTools)
- `screenshot_2.png` — заголовки example.com
- `screenshot_3.png` — заголовки [сайт 3]
- `curl_output.txt` — вывод команд curl (опционально)
