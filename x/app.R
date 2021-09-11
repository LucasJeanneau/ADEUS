library(shiny)
library(shinyWidgets)

source("dataloading.R")

# Define UI for dataset viewer app ----
ui <- fluidPage(
  
  setBackgroundImage(
    src = "https://zupimages.net/up/21/32/t77n.jpg"),
  
  # App title ----
  titlePanel("ADEUS : Indicateurs de congestion"),
  
  # Sidebar layout with a input and output definitions ----
  sidebarLayout(
    
    # Sidebar panel for inputs ----
    sidebarPanel(
    
      
      # Input: Selector for choosing dataset ----
      selectInput(inputId = "dataset",
                  label = "Choisir un indicateur:",
                  choices = c(
                              "vitesse moyenne le samedi sur 24h",
                              "vitesse moyenne mardi/jeudi sur 24h",
                              "vitesse moyenne vacances scolaires 24h",
                              "vitesse moyenne mardi/jeudi heures creuses",
                              "vitesse moyenne mardi/jeudi heures de pointe du matin",
                              "vitesse moyenne mardi/jeudi heures de pointe du soir",
                              
                              "vitesse mediane le samedi sur 24h",
                              "vitesse mediane mardi/jeudi sur 24h",
                              "vitesse mediane vacances scolaires 24h",
                              "vitesse mediane samedi heures creuses",
                              "vitesse mediane samedi heures de pointe du soir",
                              "vitesse mediane mardi/jeudi heures creuses",
                              "vitesse mediane mardi/jeudi heures de pointe du matin",
                              "vitesse mediane mardi/jeudi heures de pointe du soir",
                              
                              "nombre d'heures de congestion de niveau 1 mardi/jeudi sur 24h",
                              "nombre d'heures de congestion de niveau 2 mardi/jeudi sur 24h",
                              "nombre d'heures de congestion de niveau 3 mardi/jeudi sur 24h",
                              
                              "nombre d'heures de congestion de niveau 1 samedi sur 24h",
                              "nombre d'heures de congestion de niveau 2 samedi sur 24h",
                              "nombre d'heures de congestion de niveau 3 samedi sur 24h",
                              
                              "nombre d'heures de congestion de niveau 1 en vacances scolaires sur 24h",
                              "nombre d'heures de congestion de niveau 2 en vacances scolaires sur 24h",
                              "nombre d'heures de congestion de niveau 3 en vacances scolaires sur 24h",
                              
                              "nombre de mardi/jeudi (hors vacances scolaires) pour lesquels une congestion de niveau 3 est atteinte pendant au moins 15 min",
                              "nombre de mardi/jeudi (hors vacances scolaires) pour lesquels une congestion de niveau 3 est atteinte pendant au moins 30 min",
                              "nombre de mardi/jeudi (hors vacances scolaires) pour lesquels une congestion de niveau 3 est atteinte pendant au moins 60 min",
                              
                              "tous les indicateurs"
                        )),
      br(),
      img(src = "adeus.jpg", height = 40, width = 150),
      br(),
      br(),
      downloadButton('downloadData', 'Télécharger en format .csv')
    ),
    
    # Main panel for displaying outputs ----
    mainPanel(
      # Output: HTML table with requested number of observations ----
      tableOutput("view")

    )
  )
)

# Define server logic to summarize and view selected dataset ----
server <- function(input, output) {
  
  # Return the requested dataset ----
  datasetInput <- reactive({
    switch(input$dataset,
           "vitesse moyenne le samedi sur 24h" = dflist[20],
           "vitesse moyenne mardi/jeudi sur 24h"= dflist[19],
           "vitesse moyenne vacances scolaires 24h"= dflist[21],
           "vitesse moyenne mardi/jeudi heures creuses"= dflist[22],
           "vitesse moyenne mardi/jeudi heures de pointe du matin"= dflist[23],
           "vitesse moyenne mardi/jeudi heures de pointe du soir"= dflist[24],
           "vitesse mediane le samedi sur 24h"= dflist[12],
           "vitesse mediane mardi/jeudi sur 24h"=dflist[11],
           "vitesse mediane vacances scolaires 24h"= dflist[13],
           "vitesse mediane samedi heures creuses"= dflist[15],
           "vitesse mediane samedi heures de pointe du soir"= dflist[18],
           "vitesse mediane mardi/jeudi heures creuses"= dflist[14],
           "vitesse mediane mardi/jeudi heures de pointe du matin"= dflist[16],
           "vitesse mediane mardi/jeudi heures de pointe du soir"= dflist[17],
           
           "nombre d'heures de congestion de niveau 1 mardi/jeudi sur 24h"=dflist[1],
           "nombre d'heures de congestion de niveau 2 mardi/jeudi sur 24h"=dflist[2],
           "nombre d'heures de congestion de niveau 3 mardi/jeudi sur 24h"=dflist[3],
           
           "nombre d'heures de congestion de niveau 1 samedi sur 24h"=dflist[4],
           "nombre d'heures de congestion de niveau 2 samedi sur 24h"=dflist[5],
           "nombre d'heures de congestion de niveau 3 samedi sur 24h"=dflist[6],
           
           "nombre d'heures de congestion de niveau 1 en vacances scolaires sur 24h"=dflist[7],
           "nombre d'heures de congestion de niveau 2 en vacances scolaires sur 24h"=dflist[8],
           "nombre d'heures de congestion de niveau 3 en vacances scolaires sur 24h"=dflist[9],
           
           "nombre de mardi/jeudi (hors vacances scolaires) pour lesquels une congestion de niveau 3 est atteinte pendant au moins 15 min"=dflist[10],
           "nombre de mardi/jeudi (hors vacances scolaires) pour lesquels une congestion de niveau 3 est atteinte pendant au moins 30 min"=dflist[25],
           "nombre de mardi/jeudi (hors vacances scolaires) pour lesquels une congestion de niveau 3 est atteinte pendant au moins 60 min"=dflist[26],
           
           
           "tous les indicateurs"= all)
  })
  
  # Show observations ----
  output$view <- renderTable({
    datasetInput()
  })
  
  output$downloadData <- downloadHandler(
    filename = function() { paste(input$dataset, '.csv', sep='') },
    content = function(file) {
      write.csv(datasetInput(), file)
    }
  )
  

  
}

  
# Create Shiny app ----
shinyApp(ui = ui, server = server)