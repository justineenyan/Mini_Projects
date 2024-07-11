Public Class Form2
    Private Sub Timer1_Tick(sender As Object, e As EventArgs) Handles Timer1.Tick
        If (ProgressBar1.Value = ProgressBar1.Maximum) Then
            Timer1.Stop()
            Me.Hide()
            Form1.Show()


        Else
            ProgressBar1.PerformStep()
            lblpercent.Text = ProgressBar1.Value & ("%")
        End If
    End Sub

    Private Sub Form2_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Timer1.Start()

    End Sub

    Private Sub lblpercent_Click(sender As Object, e As EventArgs) Handles lblpercent.Click

    End Sub
End Class