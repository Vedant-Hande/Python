Public Class Form1

    Private Sub Timer1_Tick(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Timer1.Tick

        ProgressBar1.Increment(10)
        If ProgressBar1.Value = ProgressBar1.Maximum Then
            ProgressBar1.Value = 0
            Timer1.Stop()
            ProgressBar1.Hide()
            Button1.Enabled = True
        End If
    End Sub

    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

        ProgressBar1.Maximum = 100
        ProgressBar1.Minimum = 0
        Timer1.Start()

    End Sub

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click


        Form3.Show()

    End Sub
End Class
