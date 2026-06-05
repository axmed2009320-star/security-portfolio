# log_analyzer.py - Простой анализатор логов на аномалии

def analyze_logs(log_file):
    print(f"Анализ логов: {log_file}\n")
    
    with open(log_file, 'r') as f:
        lines = f.readlines()
    
    sql_count = 0
    xss_count = 0
    ip_count = {}
    
    for line in lines:
        # Ищем SQL Injection (кавычки, OR, UNION)
        if "'" in line or "OR" in line or "UNION" in line:
            print(f"[!] SQLi: {line.strip()}")
            sql_count += 1
        
        # Ищем XSS (скрипты)
        if "<script>" in line or "onerror" in line:
            print(f"[!] XSS: {line.strip()}")
            xss_count += 1
        
        # Считаем запросы по IP
        ip = line.split()[0]
        ip_count[ip] = ip_count.get(ip, 0) + 1
    
    print(f"\nСтатистика:")
    print(f"  SQLi атак: {sql_count}")
    print(f"  XSS атак: {xss_count}")
    
    print(f"\nПодозрительные IP (более 3 запросов):")
    for ip, count in ip_count.items():
        if count > 3:
            print(f"  {ip}: {count} запросов")

if __name__ == "__main__":
    analyze_logs("access.log")