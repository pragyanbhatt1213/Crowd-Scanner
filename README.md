## Crowd Scanner: Real-Time Crowd Detection with YOLOv8 \& Night Vision

Welcome to **Crowd Scanner** – a cutting-edge, real-time crowd detection and counting system that leverages the power of YOLOv8 and night vision technology. This project is designed to address the critical need for robust crowd monitoring in both daylight and low-visibility conditions, making it ideal for urban management, event security, and emergency response.

---

### 🚀 Key Features

- **State-of-the-Art Deep Learning:** Utilizes YOLOv8, the latest in real-time object detection, for highly accurate people detection and counting.
- **Night Vision Integration:** Outperforms traditional models by maintaining high accuracy even in low-light and nighttime environments.
- **Robust Dataset \& Annotation:** Trained on a diverse, custom-collected dataset spanning various crowd densities, lighting conditions, and real-world scenarios.
- **Superior Performance:** Achieves 90% accuracy, 94% precision, 92.2% recall, and a 93.1% F1 score-surpassing many existing crowd detection methods.
- **Real-World Ready:** Designed for deployment in surveillance, disaster management, and large-scale event monitoring.
- **Extensive Evaluation:** Benchmarked against leading techniques and validated on multiple datasets for reliability and generalization.
- **Scalable \& Fast:** Optimized for real-time operation with GPU acceleration and efficient data processing pipelines.

---

### 📊 Results at a Glance

| Method | Accuracy | Precision | Recall | F1 Score |
| :-- | :-- | :-- | :-- | :-- |
| **Crowd Scanner (YOLOv8 + Night Vision)** | 90% | 94.0% | 92.2% | 93.1% |
| Indoor Regional People Counting (UWB Radar) | 84% | 91.3% | 87.5% | 89.4% |
| RF-Based Device-Free Counting (HOD Features) | 76% | 84.4% | 88.4% | 86.3% |
| Cross-Camera Multiview People Counting | 90% | 93.8% | 91.8% | 92.8% |

Our model consistently outperforms or matches the best-in-class, especially in challenging lighting conditions[^1].

---

### 💡 Why Recruiters Will Love This Project

**Technical Depth \& Modern Stack**

- Deep learning (YOLOv8, transfer learning, CNNs)
- Computer vision (OpenCV, annotation with CVAT)
- Data engineering (custom dataset creation, augmentation)
- Real-time processing and GPU optimization

**Problem Solving \& Impact**

- Tackles real-world challenges: low-light detection, dense crowds, occlusions, and dynamic environments
- Demonstrates end-to-end pipeline: data collection → annotation → model training → evaluation → deployment

**Research \& Benchmarking**

- Comprehensive evaluation against state-of-the-art methods
- Detailed performance metrics and visualizations
- Clear roadmap for future improvements (sensor fusion, multi-modal detection, real-time optimization)

**Teamwork \& Project Management**

- Collaborative development with clear roles and responsibilities
- Well-documented codebase and reproducible experiments

---

### 🧑‍💻 How It Works

1. **Data Collection:** Images captured in diverse environments (classrooms, corridors, night scenes with night vision cameras)
2. **Annotation:** Bounding boxes and class labels using CVAT
3. **Model Training:** Transfer learning on YOLOv8, data augmentation, hyperparameter tuning, GPU acceleration
4. **Evaluation:** Precision, recall, F1, mAP, and confusion matrices-tested in both day and night conditions
5. **Deployment:** Real-time predictions with robust performance in surveillance and event management scenarios

---

### 📈 Visual Results

- Training and validation loss curves demonstrate consistent learning and generalization
- Confusion matrices and sample predictions show high accuracy across categories
- Visualizations included in the repo for transparency and insight

---

### 🔭 Future Directions

- **Sensor Fusion:** Integrate thermal/depth sensors for even better performance in extreme conditions
- **Dynamic Crowd Modeling:** Enhance robustness in highly dense or occluded scenarios
- **Real-Time Optimization:** Further reduce latency for large-scale deployments
- **Multi-Modal Detection:** Expand to additional input types for broader applicability

---

### 📂 Get Started

Clone the repository and follow the setup instructions in [`INSTALL.md`](INSTALL.md) to run the model on your own data or contribute to ongoing development.

---

### 🤝 Contributing

We welcome contributions! Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) for guidelines.

---

### 📣 Contact

For questions, collaborations, or demo requests, reach out via [GitHub Issues](https://github.com/pragyanbhatt1213/Crowd-Scanner/issues).

---

> **Crowd Scanner**
