from app.utils.model.model_train import train_model, resume_train_model


if __name__ == "__main__":
    resume_train_model(model_path=r"AI\runs\standoff_yolo11m_V\weights\last.pt")