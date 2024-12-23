import streamlit as st
import os
from PIL import Image
import pandas as pd

def main():
    # Define pathways data
    pathways = {
        "Pathway 1": {
            "ligands": ["Slit1", "Slit2", "Slit3"],
            "receptors": ["Robo1", "Robo2", "Robo3", "Robo4"]
        },
        "Pathway 2": {
            "ligands": ["Ntn1", "Ntn4"],
            "receptors": ["Flrt2", "Dcc", "Dscam", "Draxin", "Neo1", "Unc5a", "Unc5b", "Unc5c"]
        },
        "Pathway 3": {
            "ligands": ["Cxcl12"],
            "receptors": ["Cxcr4", "Ackr3"]
        }
    }
    
    distances = [25, 50, 75, 100]

    base_dir = os.path.dirname(__file__)

    metrics_file = os.path.join(base_dir, "ligand_receptor_metrics.csv")

    if os.path.exists(metrics_file):
        metrics_df = pd.read_csv(metrics_file)
    else:
        st.error("Metrics file not found. Please ensure 'ligand_receptor_metrics.csv' is in the app directory.")
        return
    metrics_file2 = os.path.join(base_dir, "receptor_ligand_metrics.csv")

    if os.path.exists(metrics_file2):
        metrics_df2 = pd.read_csv(metrics_file2)
    else:
        st.error("Metrics file not found. Please ensure 'ligand_receptor_metrics.csv' is in the app directory.")
        return
    


    # App title
    st.title("Pathway Selector App")

    # Pathway selection
    pathway = st.selectbox("Select a Pathway", options=list(pathways.keys()))

    # Ligand selection
    ligand = st.selectbox("Select a Ligand", options=pathways[pathway]["ligands"])

    # Receptor selection
    receptor = st.selectbox("Select a Receptor", options=pathways[pathway]["receptors"])

    # Distance selection
    distance = st.slider("Select Distance", min_value=25, max_value=100, step=25)

    # Display selected options
    st.write("## Selected Parameters")
    st.write(f"- **Pathway**: {pathway}")
    st.write(f"- **Ligand**: {ligand}")
    st.write(f"- **Receptor**: {receptor}")
    st.write(f"- **Distance**: {distance} microns")

    # Construct the file path for the histogram
    base_dir = os.path.dirname(__file__)
    histograms_dir = os.path.join(base_dir, "histograms")
    interaction_dir = os.path.join(base_dir, "new_figures")
    file_name = f"{pathway}_{receptor}_{ligand}_distance_{distance}.png"
    file_path = os.path.join(histograms_dir, file_name)
    file_name2 = f"{pathway}_{ligand}_{receptor}_distance_{distance}.png"
    file_path2= os.path.join(histograms_dir, file_name2)

    file_name3 = f"{ligand}-{receptor}_{distance}_Plot1_lr.png"
    file_path3= os.path.join(interaction_dir, file_name3)
    
    file_name4 = f"{receptor}-{ligand}_{distance}_Plot1_rl.png"
    file_path4 = os.path.join(interaction_dir, file_name4)
    

    # Check if the file exists and display the plot
    if os.path.exists(file_path):
        st.write("## Histogram")
        image = Image.open(file_path)
        st.write(f' Ligand - receptor {ligand}_{receptor} plot')
        st.image(image, caption=file_name, use_column_width=True)
    else:
        st.write("No histogram available for the selected parameters.")

    if os.path.exists(file_path3):
        st.write("## Ligand - Receptor interaction PLot")
        image = Image.open(file_path3)
        st.write(f' Ligand - receptor {ligand}_{receptor} interaction plot')
        st.image(image, caption=file_name, use_column_width=True)
    else:
        st.write("No interaction available for the selected parameters.")
    
    st.write("## Metrics")
    filtered_metrics = metrics_df[(metrics_df["Ligand"] == ligand) & 
                                  (metrics_df["Receptor"] == receptor) & 
                                  (metrics_df["Pathway Name"] == pathway) & 
                                  (metrics_df["Distance"] == distance)]

    if not filtered_metrics.empty:
        st.dataframe(filtered_metrics)
    else:
        st.write("No metrics available for the selected parameters.")

        
    if os.path.exists(file_path2):
        st.write("## Histogram")
        image = Image.open(file_path2)
        st.write(f' Ligand - receptor {receptor}_{ligand} plot')
        st.image(image, caption=file_name2, use_column_width=True)
    else:
        st.write("No histogram available for the selected parameters.")

    if os.path.exists(file_path4):
        st.write("## Receptor - Ligand interaction PLot")
        image = Image.open(file_path4)
        st.write(f' receptor - ligand {receptor}_{ligand} interaction plot')
        st.image(image, caption=file_name, use_column_width=True)
    else:
        st.write("No interaction available for the selected parameters.")
    

    filtered_metrics2 = metrics_df2[(metrics_df2["ligand"] == ligand) & 
                                  (metrics_df2["receptor"] == receptor) & 
                                  (metrics_df2["Pathway Name"] == pathway) & 
                                  (metrics_df2["Distance"] == distance)]

    st.write("## Metrics")
    if not filtered_metrics2.empty:
        st.dataframe(filtered_metrics2)
    else:
        st.write("No metrics available for the selected parameters.")

    

if __name__ == "__main__":
    main()
