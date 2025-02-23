# 🚀 KeleaCare

## 📓 Descripción
KeleaCare es un sistema inteligente de apoyo emocional que interactúa de manera empática con los usuarios, perfilando su personalidad y ofreciendo respuestas personalizadas y objetivos para su crecimiento personal.

Este proyecto fue desarrollado como parte de **HackUDC 2025**, con el objetivo de proporcionar un **chatbot de apoyo emocional** que detecte y responda a emociones de forma adaptativa.

## 👥 Participantes
- Angel Diaz Fernández | [@AngelDF00](https://github.com/AngelDF00)
- Jose Martinez Estevez | [@Joseemartinezz](https://github.com/Joseemartinezz)
- Daniel Quinteiro Graña | [@Maveriick123](https://github.com/Maveriick123)

## ✨ Características principales
- 🤖 **Chatbot de Apoyo Emocional**: análisis de sentimientos y emociones en tiempo real, con respuestas adaptadas a la emoción detectada.
- 📔 **Diario Emocional Inteligente**: permite registrar emociones y almacenar tendencias a lo largo del tiempo.
- 🎯 **Sistema de Perfilado de Personalidad**: basado en modelos psicológicos como Eneagrama y Big Five.
- 📢 **Coach de Bienestar y Objetivos**: generación de recomendaciones personalizadas según el estado emocional detectado.

## 🛠 Tecnologías Utilizadas
- **Procesamiento de lenguaje natural (NLP)**: Vader, text2emotion, transformers (GoEmotion), EmoRoBERTa, nltk / spaCy.
- **Modelos de Lenguaje**: Vicuna, LLaMA 2, Mistral, DeepSeek.
- **Almacenamiento**: bases de datos vectoriales (Weaviate, FAISS), JSON, SQL.
- **Interfaz**: Streamlit, FastAPI, React.

## 📂 Instalación y Configuración
1. Clonar este repositorio:
   ```bash
   git clone https://github.com/tuusuario/KeleaCare2.git
   cd KeleaCare2
   ```
2. Instalar las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecutar el servidor:
   ```bash
   uvicorn main:app --reload
   ```
4. Abrir la interfaz en el navegador:
   ```
   http://127.0.0.1:8000
   ```

## 📁 Estructura del Proyecto
```
keleacare/
│── backend/              # API y procesamiento de datos
│── frontend/             # Interfaz de usuario y componentes visuales
│── models/               # Modelos de NLP y análisis emocional
│── database/             # Almacenamiento de datos
│── README.md             # Documentación
│── CONTRIBUTING.md       # Guía para contribuir al proyecto
│── CODE_OF_CONDUCT.md    # Código de conducta
│── SECURITY.md           # Políticas de seguridad
```

## 🤝 Contribución
Si quieres ayudar a mejorar **KeleaCare**, sigue estos pasos:
1. Haz un fork del repositorio.
2. Crea una nueva rama para tu funcionalidad (`git checkout -b feature-nueva`).
3. Realiza tus cambios y haz un commit (`git commit -m 'Añadir nueva funcionalidad'`).
4. Envía un pull request.

Revisa el archivo [CONTRIBUTING.md](./CONTRIBUTING.md) para conocer más detalles sobre el proceso de contribución. 🎉

## 🔒 Seguridad
Si detectas algún problema de seguridad, revisa [SECURITY.md](./SECURITY.md) para saber cómo reportarlo de manera segura. Tu ayuda es clave para mantener este proyecto confiable. 🔐

## 📜 Licencia
Este proyecto está licenciado bajo [nombre de la licencia], ver el archivo [LICENSE](./LICENSE) para más detalles.

## 📩 Contacto
Para cualquier duda o sugerencia, puedes contactar con nosotros mediante los correos proporcionados en el apartado de participantes. 🚀

