import bip39
from bip32 import BIP32

def mnemonic_to_private_key(mnemonic, path="m/44'/60'/0'/0"):
    """
    Конвертирует мнемоническую фразу в приватный ключ.

    :param mnemonic: Мнемоническая фраза.
    :param path: Путь BIP32 для генерации ключа (по умолчанию для Ethereum).
    :return: Приватный ключ.
    """
    # Генерация seed из мнемонической фразы
    seed = bip39.mnemonic_to_seed(mnemonic)

    # Создание корневого ключа BIP32 из seed
    root_key = BIP32.from_seed(seed)

    # Генерация приватного ключа по указанному пути
    derived_key = root_key.get_xpriv_from_path(path)
    return derived_key

def process_mnemonics_file(input_file, output_file, path="m/44'/60'/0'/0"):
    """
    Обрабатывает файл с мнемоническими фразами и сохраняет приватные ключи в файл.

    :param input_file: Файл с мнемоническими фразами.
    :param output_file: Файл для сохранения приватных ключей.
    :param path: Путь BIP32 для генерации ключей.
    """
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            mnemonic = line.strip()  # Убираем лишние пробелы и символы новой строки
            try:
                private_key = mnemonic_to_private_key(mnemonic, path)
                outfile.write(f"{private_key}\n")
            except Exception as e:
                print(f"Ошибка при обработке мнемонической фразы: {mnemonic}. Ошибка: {e}")

# Пример использования
if __name__ == "__main__":
    input_file = "mnemonic.txt"  # Файл с мнемоническими фразами
    output_file = "private.txt"  # Файл для сохранения приватных ключей
    process_mnemonics_file(input_file, output_file)
    print(f"Приватные ключи успешно сохранены в файл {output_file}")
