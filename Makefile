# Nama file Python yang akan dijalankan
PYTHON_FILE = tree.py

# Target default
all: run

# Target untuk menjalankan file Python
run:
	python $(PYTHON_FILE)

# Target untuk membersihkan (opsional, tidak ada file yang dibersihkan di sini)
clean:
	@echo "Tidak ada file untuk dibersihkan."

# Target untuk menampilkan informasi tentang penggunaan Makefile
help:
	@echo "Makefile untuk menjalankan file Python."
	@echo "Perintah:"
	@echo "  make         - Menjalankan file Python $(PYTHON_FILE)"
	@echo "  make clean   - Membersihkan (tidak ada file untuk dibersihkan)"
	@echo "  make help    - Menampilkan bantuan ini"

