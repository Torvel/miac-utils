# Instalación
- Para instalar jira en local hay que solicitar un trial (lo pide solo el tutoria)

# Flujos

- Para el flujo de JIRA es importante configurar la instancia con visibilidad y crear un token personal de acceso en el perfil del usuario
- Para el contienedor de n8n la instancia de jira estará localizable en: http://jira:8080

# Modelos
- Es importante usar un modelo (tanto local como online) que soporte tools (por ejemplo Gemma no lo hace). Es recomendable llama3.2 o Qwen. También es recomendable ejecutar modelos del mayor tamaño y contexto posible siempre que el tiempo de ejecución lo permita, ya que con valores bajos, tendrán malos resultados.
- Si usamos ollama, asegurarnos de que ejecutamos: ``` ollama serve```