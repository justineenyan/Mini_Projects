Public Class Form1
    Private Sub Button4_Click(sender As Object, e As EventArgs) Handles Button4.Click, Button8.Click
        WebBrowser1.Navigate(TextBox1.Text)
    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click, Button5.Click
        WebBrowser1.GoForward()
    End Sub

    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click, Button6.Click
        WebBrowser1.GoBack()
    End Sub

    Private Sub Button3_Click(sender As Object, e As EventArgs) Handles Button3.Click, Button7.Click
        WebBrowser1.Refresh()
    End Sub

    Private Sub WebBrowser1_Navigated(sender As Object, e As WebBrowserNavigatedEventArgs) Handles WebBrowser1.Navigated
        TextBox1.Text = WebBrowser1.Url.ToString
    End Sub

    Private Sub WebBrowser2_Navigated(sender As Object, e As WebBrowserNavigatedEventArgs) Handles WebBrowser2.Navigated
        TextBox3.Text = WebBrowser2.Url.ToString
    End Sub
End Class
