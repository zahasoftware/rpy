using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Threading;

namespace rnet.lib.Implementations
{
    public class RPYProcess : IRPYProcess, IDisposable
    {
        internal Process process;

        private AutoResetEvent outputWaitHandle;
        private AutoResetEvent errorWaitHandle;
        private AutoResetEvent[] handles;
        internal List<string> soutput = new List<string>();
        internal List<string> serror = new List<string>();

        internal StreamWriter standardInput;
        internal readonly Object @lock;
        private readonly string pythonScriptPath;

        public ISwitch Switch { get => new Switch(this); }
        public IPWM PWM { get => new PWM(this); }

        public RPYProcess(string pythonScriptPath = "rpy.py")
        {
            @lock = new object();
            this.pythonScriptPath = pythonScriptPath;
        }

        internal void BeginStandardInputWrite()
        {
            soutput.Clear();
            serror.Clear();
            if (process.HasExited)
            {
                Start();
            }
        }

        internal void EndStandardInputWrite()
        {
            WaitHandle.WaitAny(handles);
        }

        public void CleanOutputs()
        {
            soutput.Clear();
            serror.Clear();
        }

        public void Exit()
        {
            process.Kill();
            Dispose();
        }

        public void Start()
        {
            //var psi = new ProcessStartInfo();
            process = new Process();

            process.StartInfo.FileName = "python3";
            process.StartInfo.UseShellExecute = false;
            process.StartInfo.CreateNoWindow = true;
            process.StartInfo.Arguments = "rpy.py no-banner";
            process.StartInfo.RedirectStandardOutput = true;
            process.StartInfo.RedirectStandardInput = true;
            process.StartInfo.RedirectStandardError = true;

            outputWaitHandle = new AutoResetEvent(false);
            errorWaitHandle = new AutoResetEvent(false);

            handles = new[] { outputWaitHandle, errorWaitHandle };

            process.OutputDataReceived += (sender, e) =>
            {
                if (e.Data == null || e.Data == "Enter command:")
                {
                    Console.WriteLine($"Releasing stadard output, with value={e.Data}");
                    outputWaitHandle.Set();
                }
                else
                {
                    soutput.Add(e.Data?.Trim());
                }
            };
            process.ErrorDataReceived += (sender, e) =>
            {
                Console.WriteLine($"Error Data Received {e.Data}");
                if (e.Data == null)
                {
                    errorWaitHandle.Set();
                }
                else
                {
                    serror.Add(e.Data?.Trim());
                }
            };

            process.Start();
            standardInput = process.StandardInput;

            process.BeginOutputReadLine();
            process.BeginErrorReadLine();

            EndStandardInputWrite();//To receive "Enter command:" From python
        }

        public void Dispose()
        {
            process.Dispose();
            standardInput.Dispose();

            outputWaitHandle.Dispose();
            errorWaitHandle.Dispose();
        }
    }
}
