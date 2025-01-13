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
    
    metrics_file3 = os.path.join(base_dir, "heart_only_ligand_receptor_metrics.csv")

    if os.path.exists(metrics_file3):
        metrics_df3 = pd.read_csv(metrics_file3)
    else:
        st.error("Metrics file not found. Please ensure 'ligand_receptor_metrics.csv' is in the app directory.")
        return

    metrics_file4 = os.path.join(base_dir, "heart_only_receptor_ligand_metrics.csv")

    if os.path.exists(metrics_file4):
        metrics_df4 = pd.read_csv(metrics_file4)
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
    
    base_dir = os.path.dirname(__file__)
    histograms_dir = os.path.join(base_dir, "histograms")
    interaction_dir = os.path.join(base_dir, "new_figures")

    ligand_figures = os.path.join(base_dir, "ligand_figures_only_heart")
    receptor_figures = os.path.join(base_dir, "receptor_figures")

    ligand_figures2 = os.path.join(base_dir, "ligand_figures")
    receptor_figures2 = os.path.join(base_dir, "receptor_figures_only_heart")

    ligand_expressing_figures = os.path.join(base_dir, "ligand_expressing_cells_RECA")
    receptor_expressing_figures = os.path.join(base_dir, "receptor_expressing_cells_LECA")

    ligand_expressing_figures_only_heart = os.path.join(base_dir, "ligand_expressing_cells_RECA_only_heart")
    receptor_expressing_figures_only_heart = os.path.join(base_dir, "receptor_expressing_cells_LECA_only_heart")

    file_name = f"{pathway}_{receptor}_{ligand}_distance_{distance}.png"
    file_path = os.path.join(histograms_dir, file_name)
    file_name2 = f"{pathway}_{ligand}_{receptor}_distance_{distance}.png"
    file_path2= os.path.join(histograms_dir, file_name2)

    file_name3 = f"{ligand}-{receptor}_{distance}_Plot1_lr.png"
    file_path3= os.path.join(interaction_dir, file_name3)
    
    file_name4 = f"{receptor}-{ligand}_{distance}_Plot1_rl.png"
    file_path4 = os.path.join(interaction_dir, file_name4)
    ##################

    file_name5 = f"{pathway}_{ligand}.png"
    file_path5 = os.path.join(ligand_figures, file_name5)

    file_name6 = f"{pathway}_{receptor}.png"
    file_path6 = os.path.join(receptor_figures, file_name6)

    file_name7 = f"{pathway}_{ligand}_{receptor}_r{distance}.png"
    file_path7 = os.path.join(ligand_expressing_figures, file_name7)

    file_name8 = f"{pathway}_{receptor}_{ligand}_r{distance}.png"
    file_path8 = os.path.join(receptor_expressing_figures, file_name8)

    file_name9 = f"Pathway 1_{ligand}_cell_count_with_boundary.png"
    file_path9 = os.path.join(ligand_figures2, file_name9)

    file_name11 = f"Pathway 1_{ligand}_expression_closeup.png"
    file_path11 = os.path.join(ligand_figures2, file_name11)

    file_name10 = f"Pathway 1_{receptor}_cell_count_with_boundary"
    file_path10 = os.path.join(receptor_figures2, file_name10)

    file_name12 = f"Pathway 1_{receptor}_expression_closeup.png"
    file_path12 = os.path.join(receptor_figures2, file_name12)

    file_name13 = f"Pathway 1_{ligand}_{receptor}_r25_HEART_ONLY_expr.png"
    file_path13 = os.path.join(ligand_expressing_figures_only_heart, file_name13)

    file_name14 = f"Pathway 1_{receptor}_{ligand}_r25_HEART_ONLY_expr.png"
    file_path14 = os.path.join(receptor_expressing_figures_only_heart, file_name14)
    


    # Check if the file exists and display the plot
    if os.path.exists(file_path5):
        st.write("## Ligand PLot")
        image = Image.open(file_path5)
        st.write(f' Ligand plot')
        st.image(image, caption=file_name, use_column_width=True)

    if os.path.exists(file_path9):
        st.write("### Ligand PLot heart 1 boundary")
        image = Image.open(file_path9)
        st.write(f' Ligand plot')
        st.image(image, caption=file_name9, use_column_width=True)
    
    if os.path.exists(file_path11):
        st.write("### Ligand PLot heart 2")
        image = Image.open(file_path11)
        st.write(f' Ligand plot')
        st.image(image, caption=file_name11, use_column_width=True)
    
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
    ###################
    if os.path.exists(file_path7):
        st.write("## Ligand expressing cells RECA PLot")
        image = Image.open(file_path7)
        st.write(f' Ligand - receptor {ligand}_{receptor} RECA plot')
        st.image(image, caption=file_name, use_column_width=True)
    else:
        st.write("No interaction available for the selected parameters.")

    if os.path.exists(file_path13):
        st.write("## Ligand expressing cells RECA PLot only heart cells")
        image = Image.open(file_path13)
        st.write(f' Ligand - receptor {ligand}_{receptor} RECA plot')
        st.image(image, caption=file_name13, use_column_width=True)
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
    
    st.write("## Metrics for heart")
    filtered_metrics2 = metrics_df3[(metrics_df3["Ligand"] == ligand) & 
                                  (metrics_df3["Receptor"] == receptor) & 
                                  (metrics_df3["Pathway Name"] == pathway) & 
                                  (metrics_df3["Distance"] == distance)]

    if not filtered_metrics2.empty:
        st.dataframe(filtered_metrics2)
    else:
        st.write("No metrics available for the selected parameters.")


    if os.path.exists(file_path6):
        st.write("## Receptor PLot")
        image = Image.open(file_path6)
        st.write(f' Receptor plot')
        st.image(image, caption=file_name6, use_column_width=True)
    
    if os.path.exists(file_path10):
        st.write("### Receptor PLot heart 1 boundary")
        image = Image.open(file_path10)
        st.image(image, caption=file_name10, use_column_width=True)
    
    if os.path.exists(file_path12):
        st.write("### Ligand PLot heart 2")
        image = Image.open(file_path12)
        st.image(image, caption=file_name12, use_column_width=True)

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

    ##########################
    if os.path.exists(file_path8):
        st.write("## Receptor expressing cells LECA PLot")
        image = Image.open(file_path8)
        st.write(f' Receptor - Ligand {ligand}_{receptor} LECA plot')
        st.image(image, caption=file_name, use_column_width=True)
    else:
        st.write("No interaction available for the selected parameters.")

    if os.path.exists(file_path14):
        st.write("## Receptor expressing cells LECA PLot only heart cells")
        image = Image.open(file_path14)
        st.write(f' Receptor - Ligand {ligand}_{receptor} RECA plot')
        st.image(image, caption=file_name14, use_column_width=True)
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
    
    st.write("## Metrics for heart")
    filtered_metrics4 = metrics_df4[(metrics_df4["Ligand"] == receptor) & 
                                  (metrics_df4["Receptor"] == ligand) & 
                                  (metrics_df4["Pathway Name"] == pathway) & 
                                  (metrics_df4["Distance"] == distance)]

    if not filtered_metrics4.empty:
        st.dataframe(filtered_metrics4)
    else:
        st.write("No metrics available for the selected parameters.")

    

if __name__ == "__main__":
    main()
