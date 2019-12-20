using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Threading;

namespace rnet.lib.Implementations.NoLive
{
    public class NoLiveProcess : IPyProcess, IDisposable
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

        public ISwitch Switch { get => new NoLiveSwitch(this); }
        public IPWM PWM { get => new NoLivePWM(this); }

        public NoLiveProcess(string pythonScriptPath = "rwy.py")
        {
            @lock = new object();
            this.pythonScriptPath = pythonScriptPath;
        }



        internal void BeginStandardInputWrite()
        {
            soutput.Clear();
            serror.Clear();
            if (!IsRunning(process))
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
        }

        public void Start()
        {
        }

        public void ExcecuteCommand(string args)
        {
            //var psi = new ProcessStartInfo();
            using (process = new Process())
            {

                if (!File.Exists(pythonScriptPath))
                {
                    throw new FileNotFoundException($"File \"{pythonScriptPath}\" doesn't exists");
                }

                process.StartInfo.FileName = "python3";
                process.StartInfo.UseShellExecute = false;
                process.StartInfo.CreateNoWindow = true;
                process.StartInfo.Arguments = $"{pythonScriptPath} {args}";
                process.StartInfo.RedirectStandardOutput = true;
                process.StartInfo.RedirectStandardInput = true;
                process.StartInfo.RedirectStandardError = true;

                process.Start();
                process.WaitForExit(10000);


                this.Dispose();
            }
        }

        public void Dispose()
        {
            process.Dispose();

        }

        public bool IsRunning(Process process)
        {
           return true;
        }
    }
}
