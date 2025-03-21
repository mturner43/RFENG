import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from io import BytesIO

st.title('RF Engineering Data Dashboard')
st.markdown(
    '''
    This dashboard is used to assist in creating various types of graphs.  
    Available Options:  
    :blue[Line plot]: generates a line graph.  
    :blue[Same X-axis]: generates a line graph with multiple lines sharing the same X-axis.  
    :blue[Same Y-axis]: generates a line graph with multiple lines sharing the same Y-axis.  
    :blue[Two Y-axis]: generates a line graph that can have multiple X and Y axes.  
    :blue[Scatter plot]: creates a scatter plot.  
      
    Instructions:  
    Just drag and drop an excel file below. Ensure all columns have a header describing the data within that column, and all headers are in row 1.    
    '''
)

uploaded_file = st.file_uploader("Choose a file", type="xlsx")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    headers = df.columns.tolist()
    st.write(df.set_index(headers[0]))
else:
    st.write(' ')

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Line plot", "Same X-axis", 'Same Y-axis','Two Y-axis', 'Scatter Plot'])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        if uploaded_file is not None:
            df = pd.read_excel(uploaded_file)
            headers = df.columns.tolist()

            x_column = st.selectbox('Select X-axis column', headers)
            y_column = st.selectbox('Select Y-axis column', headers)
            custom_title = st.text_input('Enter the title for the graph', 'Title1')
            x_label = st.text_input('Enter X-axis Label','X-Axis',key='x_axis_label')
            y_label = st.text_input('Enter Y-axis Label','Y-axis',key='y_axis_label')
            X_scale = st.selectbox('Select X-axis scale', ['linear', 'log'], key='x_scale')
            y_scale = st.selectbox('Select Y-axis scale', ['linear', 'log'], key='y_scale')
            limits = st.toggle("Edit Axis", key='tab1')
            if limits:
                x_min = st.number_input('Enter minimum x-axis limit', value=float(df[x_column].min()),key='plot1_x1')
                x_max = st.number_input('Enter maximum x-axis limit', value=float(df[x_column].max()), key='plot1_x2')
                y_min = st.number_input('Enter minimum y-axis limit', value=float(df[y_column].min()),key='plot1_y1')
                y_max = st.number_input('Enter maximum y-axis limit', value=float(df[y_column].max()),key='plot1_y2')
        else:
            st.write('Waiting on file to be uploaded')
    with col2:
        if uploaded_file is not None:
            if x_column and y_column:
                fig, ax = plt.subplots()
                ax.plot(df[x_column], df[y_column])
                ax.grid(True)
                ax.set_xlabel(x_label)
                ax.set_ylabel(y_label)
                ax.set_title(custom_title)
                ax.set_xscale(X_scale)
                ax.set_yscale(y_scale)
                st.pyplot(fig)
                buf = BytesIO()
                fig.savefig(buf,format='png')
                buf.seek(0)
                st.download_button(label='Download plot as PNG', data=buf,file_name='plot.png',mime='image/png',key='button1')
            if limits:
                fig1, ax = plt.subplots()
                ax.plot(df[x_column], df[y_column])
                ax.grid(True)
                ax.set_xlabel(x_label)
                ax.set_ylabel(y_label)
                ax.set_title(custom_title)
                ax.set_xscale(X_scale)
                ax.set_yscale(y_scale)
                ax.set_xlim([x_min, x_max])
                ax.set_ylim([y_min, y_max])
                st.pyplot(fig1)
                buf = BytesIO()
                fig1.savefig(buf,format='png')
                buf.seek(0)
                st.download_button(label='Download plot as PNG', data=buf,file_name='plot.png',mime='image/png',key='button2')
        else:
            st.write('')


with tab2:
    col1, col2 = st.columns(2)
    with col1:
        if uploaded_file is not None:
        # Read the Excel file
            df = pd.read_excel(uploaded_file)
            headers = df.columns.tolist()
        # Select column for x-axis
            x_column = st.selectbox('Select X-axis column', headers, key='x_column')
        
        # Select columns for line plots
            selected_columns = st.multiselect('Select Y-Axis', headers, key='y_columns')

            custom_title = st.text_input('Enter the title for the graph', 'Title',key='Title2')
            custom_xlabel = st.text_input('Enter X-axis Label','X-axis',key='x_axis_l')
            custom_ylabel = st.text_input('Enter Y-Axis Label','Y-axis',key='y_axis_l')
            X_scale = st.selectbox('Select X-axis scale', ['linear', 'log'], key='x1_scale')
            y_scale = st.selectbox('Select Y-axis scale', ['linear', 'log'], key='y2_scale')
            limits = st.toggle("Edit Axis", key='tab2')
            if limits:
                x_min = st.number_input('Enter minimum x-axis limit', value=float(df[x_column].min()),key='plot2_x1')
                x_max = st.number_input('Enter maximum x-axis limit', value=float(df[x_column].max()),key='plot2_x2')
                y_min = st.number_input('Enter minimum y-axis limit', value=float(df[selected_columns[0]].min()),key='plot2_y1')
                y_max = st.number_input('Enter maximum y-axis limit', value=float(df[selected_columns[0]].max()),key='plot2_y2')
        else:
            st.write('Waiting on file to be uploaded')
    with col2:
        if uploaded_file is not None:
            if x_column and selected_columns:
                fig, ax = plt.subplots()
                for column in selected_columns:
                    ax.plot(df[x_column], df[column], label=column)
                ax.grid(True)
                ax.set_xlabel(custom_xlabel)
                ax.set_ylabel(custom_ylabel)
                ax.set_title(custom_title)
                ax.set_xscale(X_scale)
                ax.set_yscale(y_scale)
                ax.legend(loc='best',fontsize='small')
                st.pyplot(fig)
                buf = BytesIO()
                fig.savefig(buf,format='png')
                buf.seek(0)
                st.download_button(label='Download plot as PNG', data=buf,file_name='plot.png',mime='image/png',key='button3')
            else:
                st.write('Please select data for the Y-axis')
            if limits:
                fig1, ax = plt.subplots()
                for column in selected_columns:
                    ax.plot(df[x_column], df[column], label=column)
                ax.grid(True)
                ax.set_xlabel(custom_xlabel)
                ax.set_ylabel(custom_ylabel)
                ax.set_title(custom_title)
                ax.set_xscale(X_scale)
                ax.set_yscale(y_scale)
                ax.set_xlim([x_min, x_max])
                ax.set_ylim([y_min, y_max])
                ax.legend(loc='best',fontsize='small')
                st.pyplot(fig1)
                buf = BytesIO()
                fig1.savefig(buf,format='png')
                buf.seek(0)
                st.download_button(label='Download plot as PNG', data=buf,file_name='plot.png',mime='image/png',key='button4')
        else: 
            st.write(" ")

with tab3:
    col1, col2 = st.columns(2)
    with col1:
        if uploaded_file is not None:
            df = pd.read_excel(uploaded_file)
            headers = df.columns.tolist()
            x_column = st.multiselect('Select X-axis', headers, key='x_columns')
            ycolumn = st.selectbox('Select Y-axis', headers, key='y_column')
            custom_title = st.text_input('Enter the title for the graph', 'Title',key='Title3')
            custom_xlabel = st.text_input('Enter X-axis Label','X-axis',key='x_axis1')
            custom_ylabel = st.text_input('Enter Y-axis Label','Y-axis',key='y_axis1')
            X_scale = st.selectbox('Select X-axis scale', ['linear', 'log'], key='x2_scale')
            y_scale = st.selectbox('Select Y-axis scale', ['linear', 'log'], key='y3_scale')
            limits = st.toggle('Edit Axis', key='tab3')
            if limits:
                x_min = st.number_input('Enter minimum x-axis limit', value=float(df[x_column[0]].min()),key='plot2_x1')
                x_max = st.number_input('Enter maximum x-axis limit', value=float(df[x_column[0]].max()),key='plot2_x2')
                y_min = st.number_input('Enter minimum y-axis limit', value=float(df[ycolumn].min()),key='plot2_y1')
                y_max = st.number_input('Enter maximum y-axis limit', value=float(df[ycolumn].max()),key='plot2_y2')
        else:
            st.write('Waiting on file to be uploaded')
    with col2:
        if uploaded_file is not None:
        # Create line plots
            if x_column and selected_columns:
                fig, ax = plt.subplots()
                for column in x_column:
                    ax.plot(df[column], df[ycolumn], label=column)
                ax.grid(True)
                ax.set_xlabel(custom_xlabel)
                ax.set_ylabel(custom_ylabel)
                ax.set_title(custom_title)
                ax.set_xscale(X_scale)
                ax.set_yscale(y_scale)
                ax.legend(loc='best', fontsize='small')
                st.pyplot(fig)
                buf = BytesIO()
                fig.savefig(buf,format='png')
                buf.seek(0)
                st.download_button(label='Download plot as PNG', data=buf,file_name='plot.png',mime='image/png',key='button5')
                if limits:
                    fig1, ax = plt.subplots()
                    for column in x_column:
                        ax.plot(df[column], df[ycolumn], label=column)
                    ax.grid(True)
                    ax.set_xlabel(custom_xlabel)
                    ax.set_ylabel(custom_ylabel)
                    ax.set_title(custom_title)
                    ax.set_xscale(X_scale)
                    ax.set_yscale(y_scale)
                    ax.set_xlim([x_min, x_max])
                    ax.set_ylim([y_min, y_max])
                    ax.legend(loc='best',fontsize='small')
                    st.pyplot(fig1)
                    buf = BytesIO()
                    fig1.savefig(buf,format='png')
                    buf.seek(0)
                    st.download_button(label='Download plot as PNG', data=buf,file_name='plot.png',mime='image/png',key='button6')

            else:
                st.write('Please select data for X-axis')
        else: 
            st.write(" ")

with tab4:
    col1, col2 = st.columns(2)
    with col1:
        if uploaded_file is not None:
            # Read the Excel file
            df = pd.read_excel(uploaded_file)
            headers = df.columns.tolist()
            
            # Select Data
            num_lines = st.number_input('Enter number of lines to plot', min_value=1, max_value=10, value=1)
            x_columns = []
            y_columns = []
            x2_columns = []
            y2_columns = []
            labels =[]
            secondary_axis = []
            for i in range(num_lines):
                x = st.selectbox(f'Select X-axis column for line {i+1}',headers, key=f'x_column_{i}')
                y = st.selectbox(f'Select Y-axis column for line {i+1}',headers, key=f'y_column_{i}')
                label = st.text_input(f'Enter Label for line {i+1}',f'Label {i+1}',key=f'label_{i}')
                Secondary = st.checkbox('Secondary Y-axis', key=f'secondary_x_axis_{i}')
                if Secondary:
                    x2_columns.append(x)
                    y2_columns.append(y)
                    labels.append(label)
                    secondary_axis.append(True)
                else:
                    x_columns.append(x)
                    y_columns.append(y)
                    labels.append(label)
                    secondary_axis.append(False)

        else:
            st.write('Waiting on file to be uploaded')
    with col2:
        if uploaded_file is not None:
            custom_title = st.text_input('Enter the title for the graph', 'Title',key='Title4')
            custom_xlabel = st.text_input('Enter X-axis Label','X-axis',key='x_axis2')
            custom_ylabel = st.text_input('Enter Primary Y-axis Label','Y-axis',key='y_axis2')
            if any(secondary_axis):
                custom_y2label = st.text_input('Enter Seondary Y-axis Label', 'Secondary Y-axis',key='y2_axis')
            X_scale = st.selectbox('Select X-axis scale', ['linear', 'log'], key='x3_scale')
            y_scale = st.selectbox('Select Y-axis scale', ['linear', 'log'], key='y4_scale')
            legend = st.selectbox('Select location of legend',['best','upper right','upper left','upper center','lower right', 'lower left', 'lower center'],key='legend')
            if any(secondary_axis):
                legend2 = st.selectbox('Select location of secondary legend',['best','upper right','upper left','upper center','lower right', 'lower left', 'lower center'],key='legend2')
            # Create line plots
            if x_columns and y_columns:
                fig, ax1 = plt.subplots()
                for i in range(len(x_columns)):
                    ax1.plot(df[x_columns[i]], df[y_columns[i]],label=labels[i])
                ax1.set_xlabel(custom_xlabel)
                ax1.set_ylabel(custom_ylabel)
                ax1.set_title(custom_title)
                ax1.set_yscale(y_scale)
                ax1.set_xscale(X_scale)
                ax1.grid(True)

                if x2_columns or y2_columns:
                    ax2 = ax1.twinx()
                    for i in range(len(x2_columns)):
                        ax2.plot(df[x2_columns[i]], df[y2_columns[i]], linestyle='--', label=labels[i+len(x_columns)])
                    ax2.set_ylabel(custom_y2label, color='blue')
                    ax2.grid(linewidth=0.5)
                    ax2.tick_params(axis='y',color='blue',labelcolor='blue')
                    ax2.legend(loc=legend2, fontsize='small')
                ax1.legend(loc=legend, fontsize='small')
                st.pyplot(fig)
                buf = BytesIO()
                fig.savefig(buf,format='png')
                buf.seek(0)
                st.download_button(label='Download plot as PNG', data=buf,file_name='plot.png',mime='image/png',key='button7')
            limits = st.toggle("Edit Axis", key='tab4')
            if limits:
                x_min = st.number_input('Enter minimum x-axis limit', value=float(df[x_columns[0]].min()),key='plot3_x1')
                x_max = st.number_input('Enter maximum x-axis limit', value=float(df[x_columns[0]].max()), key='plot3_x2')
                y_min = st.number_input('Enter minimum y-axis limit', value=float(df[y_columns[0]].min()),key='plot3_y1')
                y_max = st.number_input('Enter maximum y-axis limit', value=float(df[y_columns[0]].max()),key='plot3_y2')
                if any(secondary_axis):
                    y2_min = st.number_input('Enter minimum secondary y-axis limit', value=float(df[y2_columns[0]].min()),key='plot3_y3')
                    y2_max = st.number_input('Enter maximum secondary y-axis limit', value=float(df[y2_columns[0]].max()),key='plot3_y4')
                if x_columns and y_columns:
                    fig, ax1 = plt.subplots()
                    for i in range(len(x_columns)):
                        ax1.plot(df[x_columns[i]], df[y_columns[i]],label=labels[i])
                    ax1.set_xlabel(custom_xlabel)
                    ax1.set_ylabel(custom_ylabel)
                    ax1.set_title(custom_title)
                    ax1.set_yscale(y_scale)
                    ax1.set_xscale(X_scale)
                    ax1.set_xlim([x_min, x_max])
                    ax1.set_ylim([y_min, y_max])
                    ax1.grid(True)

                if x2_columns or y2_columns:
                    ax2 = ax1.twinx()
                    for i in range(len(x2_columns)):
                        ax2.plot(df[x2_columns[i]], df[y2_columns[i]], linestyle='--', label=labels[i+len(x_columns)])
                    ax2.set_ylabel(custom_y2label, color='blue')
                    ax2.grid(linewidth=0.5)
                    ax2.tick_params(axis='y',color='blue',labelcolor='blue')
                    ax2.set_ylim([y2_min,y2_max])
                    ax2.legend(loc=legend2, fontsize='small')
                ax1.legend(loc=legend, fontsize='small')
                st.pyplot(fig)
                buf = BytesIO()
                fig.savefig(buf,format='png')
                buf.seek(0)
                st.download_button(label='Download plot as PNG', data=buf,file_name='plot.png',mime='image/png',key='button8')
        else:
            st.write(' ')

with tab5:
    col1, col2 = st.columns(2)
    with col1:
        if uploaded_file is not None:
            df = pd.read_excel(uploaded_file)
            headers = df.columns.tolist()

            x_column = st.selectbox('Select X-axis column', headers, key='xs_column')
            y_column = st.selectbox('Select Y-axis column', headers, key='ys_column')
            custom_title = st.text_input('Enter the title for the graph', 'Title5')
            custom_xlabel = st.text_input('Enter X-axis Label','X-axis',key='xs_axis')
            custom_ylabel = st.text_input('Enter Y-axis Label','Y-axis',key='ys_axis')
            X_scale = st.selectbox('Select X-axis scale', ['linear', 'log'], key='xs_scale')
            y_scale = st.selectbox('Select Y-axis scale', ['linear', 'log'], key='ys_scale')
            limits = st.toggle("Edit Axis", key='tab5')
            if limits:
                x_min = st.number_input('Enter minimum x-axis limit', value=float(df[x_column].min()),key='plot4_x1')
                x_max = st.number_input('Enter maximum x-axis limit', value=float(df[x_column].max()), key='plot4_x2')
                y_min = st.number_input('Enter minimum y-axis limit', value=float(df[y_column].min()),key='plot4_y1')
                y_max = st.number_input('Enter maximum y-axis limit', value=float(df[y_column].max()),key='plot4_y2')
        else:
            st.write('Waiting on the file to be uploaded')
    with col2:
        if uploaded_file is not None:
            if x_column and y_column:
                fig, ax = plt.subplots()
                ax.scatter(df[x_column], df[y_column])
                ax.grid(True)
                ax.set_xlabel(custom_xlabel)
                ax.set_ylabel(custom_ylabel)
                ax.set_title(custom_title)
                ax.set_xscale(X_scale)
                ax.set_yscale(y_scale)
                st.pyplot(fig)

                buf = BytesIO()
                fig.savefig(buf,format='png')
                buf.seek(0)

                st.download_button(label='Download plot as PNG', data=buf,file_name='plot.png',mime='image/png',key='button9')

            if limits:
                fig1, ax = plt.subplots()
                ax.scatter(df[x_column], df[y_column],label=y_column)
                ax.grid(True)
                ax.set_xlabel(custom_xlabel)
                ax.set_ylabel(custom_ylabel)
                ax.set_title(custom_title)
                ax.set_yscale(y_scale)
                ax.set_xlim([x_min, x_max])
                ax.set_ylim([y_min, y_max])
                st.pyplot(fig1)

                buf = BytesIO()
                fig1.savefig(buf,format='png')
                buf.seek(0)

                st.download_button(label='Download plot as PNG', data=buf,file_name='plot.png',mime='image/png',key='button10')
        else:
            st.write('')