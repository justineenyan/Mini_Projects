Public Class splash_1
    Private Sub Timer1_Tick(sender As Object, e As EventArgs) Handles Timer1.Tick
        If (ProgressBar1.Value = ProgressBar1.Maximum) Then
            Timer1.Stop()
            Me.Hide()
            BROWSER.Show()


        Else
            ProgressBar1.PerformStep()
            lblpercent.Text = ProgressBar1.Value & ("%")
        End If
    End Sub

    Private Sub splash_1_Load(sender As Object, e As EventArgs) Handles MyBase.Load

        Timer1.Start()

    End Sub
End Class
