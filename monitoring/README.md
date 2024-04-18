

# se déplacer dans le dossier monitoring et pour voir le dashboard : 
streamlit run monitoring/dashboard.py

Après avoir créer les dossiers et fichiers du container monitoring 
docker build -t streamlit_app .  pour construire l'image du container puis run l'image
sudo docker run -p 8501:8501 streamlitapp:latest


streamlit run monitoring/dashboard.py

Pour connecter streamlit à postgresql : 
https://docs.streamlit.io/develop/tutorials/databases/postgresql#write-your-streamlit-app