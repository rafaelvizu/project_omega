# Project Omega

## Dependências

- [Python 3.10](https://www.python.org/downloads/release/python-3110/)
- [opencv-python](https://pypi.org/project/opencv-python/)
- [dlib](https://pypi.org/project/dlib/)
- [face_recognition](https://pypi.org/project/face_recognition/)
- [flask](https://pypi.org/project/Flask/)
- [opencv-python](https://pypi.org/project/opencv-python/)
- [os](https://docs.python.org/3/library/os.html)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Notas

- Para executar, inicie o arquivo `/src/main.py` com o comando `python src/main.py` no terminal.

- Caso ocorra um erro na instalação do `dlib`, execute o comando `pip install https://github.com/jloh02/dlib/releases/download/v19.22/dlib-19.22.99-cp310-cp310-win_amd64.whl`.

- Lembre-se de criar um ambiente virtual para instalar as dependências `python -m venv env` e ativar o ambiente `env\Scripts\activate`.

- Crie um arquivo `.env` na raiz do projeto e adicione a variável `RTSP_URL` com o endereço RTSP da câmera.
