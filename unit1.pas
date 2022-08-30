unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, FileUtil, Forms, Controls,
  Dialogs,
  ClipBrd,
  math,
  StdCtrls;


type

  { TForm1 }

  TForm1 = class(TForm)
    EditCM: TEdit;
    EditNM: TEdit;
    EditEV: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    Label4: TLabel;
    procedure EditCMChange(Sender: TObject);
    procedure EditCMKeyPress(Sender: TObject; var Key: char);
    procedure EditNMChange(Sender: TObject);
    procedure EditNMKeyPress(Sender: TObject; var Key: char);
    procedure EditEVChange(Sender: TObject);
    procedure EditEVKeyPress(Sender: TObject; var Key: char);
    function ValidFloat(Value: string): Boolean;
    function getRoundUnc(str: string): Double;
    function roundValue(Val, uncVal: Double): string;
    function NM_2_CM(str: string): string;
    function NM_2_EV(str: string): string;
    function CM_2_NM(str: string): string;
    function CM_2_EV(str: string): string;
    function EV_2_CM(str: string): string;
    function EV_2_NM(str: string): string;
  private

  public

  end;

var
  Form1: TForm1;
  Fh : Double = 6.626070040e-34;
  Fc : Double = 299792458;
  Fe : Double = 1.6021766208e-19;

implementation

{$R *.lfm}

{ TForm1 }


procedure TForm1.EditCMChange(Sender: TObject);
begin
   if (EditCM.Text <> '') and EditCM.Focused then
    if ValidFloat(EditCM.Text) then
     if StrToFloat(EditCM.Text) > 0 then
      begin
       EditNM.Text := CM_2_NM(EditCM.Text);
       EditEV.Text := CM_2_EV(EditCM.Text);
      end
     else
      begin
       EditNM.Text := '';
       EditEV.Text := '';
      end
    else
     begin
      EditNM.Text := '';
      EditEV.Text := '';
     end;
end;

procedure TForm1.EditNMChange(Sender: TObject);
begin
   if (EditNM.Text <> '') and EditNM.Focused then
    if ValidFloat(EditNM.Text) then
     if StrToFloat(EditNM.Text) > 0 then
      begin
       EditCM.Text := NM_2_CM(EditNM.Text);
       EditEV.Text := NM_2_EV(EditNM.Text);
      end
     else
      begin
       EditCM.Text := '';
       EditEV.Text := '';
      end
    else
     begin
      EditCM.Text := '';
      EditEV.Text := '';
     end;
end;

procedure TForm1.EditEVChange(Sender: TObject);
begin
   if (EditEV.Text <> '') and EditEV.Focused then
  if ValidFloat(EditEV.Text) then
   if StrToFloat(EditEV.Text) > 0 then
    begin
     EditCM.Text := EV_2_CM(EditEV.Text);
     EditNM.Text := EV_2_NM(EditEV.Text);
    end
   else
    begin
     EditCM.Text := '';
     EditNM.Text := '';
    end
  else
   begin
    EditCM.Text := '';
    EditNM.Text := '';
   end;
end;

procedure TForm1.EditNMKeyPress(Sender: TObject; var Key: char);
begin
   case key of
    #27: Application.Terminate;
    '0'..'9': ;
    #8: ;
    #3: Clipboard.AsText:=EditNM.SelText;
    '.', ',': begin if Pos(DefaultFormatSettings.DecimalSeparator, EditNM.Text) = 0 then Key := DefaultFormatSettings.DecimalSeparator
        else Key := #0; end;
    else key := #0;
  end;
end;

procedure TForm1.EditCMKeyPress(Sender: TObject; var Key: char);
begin
   case key of
    #27: Application.Terminate;
    '0'..'9': ;
    #8: ;
    #3: Clipboard.AsText:=EditCM.SelText;
    '.', ',': begin
                if Pos(DefaultFormatSettings.DecimalSeparator, EditCM.Text) = 0 then
                    Key := DefaultFormatSettings.DecimalSeparator
                else Key := #0;
              end;
    else key := #0;
  end;
end;

procedure TForm1.EditEVKeyPress(Sender: TObject; var Key: char);
begin
   case key of
    #27: Application.Terminate;
    '0'..'9': ;
    #8: ;
    #3: Clipboard.AsText:=EditEV.SelText;
    '.', ',': begin if Pos(DefaultFormatSettings.DecimalSeparator, EditEV.Text) = 0 then Key := DefaultFormatSettings.DecimalSeparator
        else Key := #0; end;
    else key := #0;
  end;
end;


function TForm1.ValidFloat(Value: string): Boolean;
begin
 Result := True;
 try
  StrToFloat(Value);
 except
  on E: EConvertError do
   begin
    Result := False;
   end;
 end;
end;

function TForm1.NM_2_CM(str: string): string;
var
  Val, uncVal: Double;
begin
  Val := 1e7 / StrToFloat(str);
  uncVal := 1e7 * getRoundUnc(str) / (StrToFloat(str) * StrToFloat(str));
  Result := roundValue(Val, uncVal);
end;

function TForm1.CM_2_NM(str: string): string;
var
  Val, uncVal: Double;
begin
  Val := 1e7 / StrToFloat(str);
  uncVal := 1e7 * getRoundUnc(str) / (StrToFloat(str) * StrToFloat(str));
  Result := roundValue(Val, uncVal);
end;

function TForm1.NM_2_EV(str: string): string;
var
  Val, uncVal, scaleF: Double;
begin
  scaleF := Fh * Fc / (1e-9 * Fe);
  Val := scaleF / StrToFloat(str);
  uncVal := scaleF * getRoundUnc(str) / (StrToFloat(str) * StrToFloat(str));
  Result := roundValue(Val, uncVal);
end;

function TForm1.CM_2_EV(str: string): string;
var
  Val, uncVal, scaleF: Double;
begin
  scaleF := Fh * Fc / (1e-2 * Fe);
  Val := scaleF * StrToFloat(str);
  uncVal := scaleF * getRoundUnc(str);
  Result := roundValue(Val, uncVal);
end;

function TForm1.EV_2_CM(str: string): string;
var
  Val, uncVal, scaleF: Double;
begin
  scaleF := 1e-2 * Fe / (Fh * Fc);
  Val := scaleF * StrToFloat(str);
  uncVal := scaleF * getRoundUnc(str);
  Result := roundValue(Val, uncVal);
end;

function TForm1.EV_2_NM(str: string): string;
var
  Val, uncVal, scaleF: Double;
begin
  scaleF := Fh * Fc / (1e-9 * Fe);
  Val := scaleF / StrToFloat(str);
  uncVal := scaleF * getRoundUnc(str) / (StrToFloat(str) * StrToFloat(str));
  Result := roundValue(Val, uncVal);
end;


function TForm1.getRoundUnc(str: string): Double;
// get the rounding uncertainty from the float which is in string variable
var
  digits: Integer;
begin
  if Pos(DefaultFormatSettings.DecimalSeparator, str) = 0 then
    digits := 0
  else
    digits := Length(str) - Pos(DefaultFormatSettings.DecimalSeparator, str);
  Result := Power(10, - digits) * 0.5;
end;


function TForm1.roundValue(Val, uncVal: Double): string;
// round Val to the place of two significant digits of uncVal
var
  decPlace: Integer;
  str: string;
begin
  decPlace := 1 - Floor(Log10(uncVal));
  if decPlace < 0 then
    str := FloatToStrF(Val, ffFixed, 16, 0)
  else
    str := FloatToStrF(Val, ffFixed, 16, decPlace);
  Result := str;
end;


end.

