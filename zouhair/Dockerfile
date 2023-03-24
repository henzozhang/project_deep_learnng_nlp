# # Use the official TensorFlow Serving image as the base image
# FROM tensorflow/serving
# # Set the environment variable for the model name
# ENV MODEL_NAME=hugging_model

# # Copy the exported model files to the appropriate location in the container
# COPY exported_model/hugging_model /models/$MODEL_NAME/1/

# # Update package repositories
# RUN apt-get update

# # Install build-essential and python3-dev
# RUN apt-get install -y build-essential python3-dev

# # Install Python 3 and pip
# RUN apt-get update && apt-get install -y --no-install-recommends python3 python3-pip

# # Install setuptools
# RUN pip3 install setuptools



# # Install Python packages
# RUN pip3 install setuptools_rust
# RUN pip3 install requests
# # RUN pip3 install torch
# # RUN pip3 install tensorflow==2.11.0
# RUN pip3 install transformers
# RUN pip3 install tokenizers




# # Expose ports for RESTful API (8501) and gRPC (8500)
# EXPOSE 8500 8501

# # Start the TensorFlow Serving server
# CMD tensorflow_model_server --port=8500 --rest_api_port=8501 --model_name=$hugging_model --model_base_path=/models/$hugging_model

# # Start the TensorFlow Serving server

# FROM tensorflow/serving:2.6.0

# WORKDIR /app

# COPY .. /app/exported_model
# COPY requirements.txt /app

# RUN apt-get update --no-cache && \
#     apt-get install -y gnupg && \
#     apt-get install -y python3-pip

# RUN pip3 install -r requirements.txt

# EXPOSE 8500

# CMD tensorflow_model_server --rest_api_port=8501 --model_name=$hugging_model --model_base_path=/models/$hugging_model

# Base image
# FROM tensorflow/serving

# # Create a working directory
# WORKDIR /app

# # Copy the exported model to the container
# COPY ./exported_model/hugging_model /models/hugging_model

# # Create a configuration file
# RUN echo '{ "model_config_list": [ { "name": "hugging_model", "base_path": "/models/hugging_model", "model_platform": "tensorflow" } ] }' > /models/models.config


# # Expose the port for the API
# EXPOSE 8501

# # Start the TensorFlow Serving server
# CMD ["tensorflow_model_server", "--port=8500", "--rest_api_port=8501", "--model_config_file=/models/models.config"]

FROM tensorflow/serving

# Create a working directory
WORKDIR /app

# Copy the exported model to the container
COPY ./exported_model/hugging_model/saved_model/1 /models/hugging_model/saved_model/1

# Create a configuration file
RUN echo 'model_config_list { config { name: "hugging_model", base_path: "/models/hugging_model", model_platform: "tensorflow" } }' > /models/models.config

# Expose the port for the API
EXPOSE 8501

# Start the TensorFlow Serving server
CMD ["tensorflow_model_server", "--port=8500", "--rest_api_port=8501", "--model_config_file=/models/models.config"]